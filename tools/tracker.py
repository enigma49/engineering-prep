#!/usr/bin/env python3
"""A small, evidence-based study log. Python 3.9+; standard library only."""

from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError


PROJECT_ROOT = Path(__file__).resolve().parents[1]
INTERVALS = (1, 3, 7, 14, 30)
OUTCOMES = ("learned", "independent", "hinted", "needs_review")
LABELS = {
    "learned": "Studied with explanation",
    "independent": "Independent on latest attempt",
    "hinted": "Attempted with hints",
    "needs_review": "Needs review",
}


class TrackerError(Exception):
    """An actionable input or state error, displayed without a traceback."""


@dataclass(frozen=True)
class ReviewState:
    last_date: date
    outcome: str
    stage: int
    due: date
    evidence: str


def local_today() -> date:
    try:
        return datetime.now(ZoneInfo("Asia/Kolkata")).date()
    except ZoneInfoNotFoundError as exc:
        raise TrackerError("Asia/Kolkata timezone data is unavailable on this Python installation.") from exc


def parse_date(value: str) -> date:
    try:
        parsed = date.fromisoformat(value)
    except (ValueError, TypeError) as exc:
        raise TrackerError(f"Invalid date {value!r}; use YYYY-MM-DD.") from exc
    if parsed.isoformat() != value:
        raise TrackerError(f"Invalid date {value!r}; use YYYY-MM-DD.")
    return parsed


def read_json(path: Path) -> Any:
    try:
        with path.open(encoding="utf-8") as handle:
            return json.load(handle)
    except (OSError, UnicodeError, json.JSONDecodeError) as exc:
        raise TrackerError(f"Cannot read {path.name}: {exc}. Existing data was not changed.") from exc


def nonempty_text(value: Any, field: str) -> str:
    if not isinstance(value, str) or not value.strip():
        raise TrackerError(f"{field} must be a nonempty string.")
    return value.strip()


def load_catalog(root: Path) -> dict[str, dict[str, Any]]:
    items: dict[str, dict[str, Any]] = {}
    for filename, kind in (("neetcode150.json", "problem"), ("topics.json", "topic")):
        rows = read_json(root / "data" / filename)
        if not isinstance(rows, list):
            raise TrackerError(f"{filename} must contain a JSON array.")
        for row in rows:
            if not isinstance(row, dict):
                raise TrackerError(f"Each entry in {filename} must be an object.")
            item_id = nonempty_text(row.get("id"), f"{filename} id")
            title = nonempty_text(row.get("title"), f"{filename} title")
            if row["id"] != item_id or item_id in items:
                raise TrackerError(f"Duplicate or whitespace-padded catalog ID: {item_id!r}.")
            items[item_id] = {**row, "title": title, "kind": kind}
    return items


def validate_events(events: Any, catalog: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    if not isinstance(events, list):
        raise TrackerError("reviews.json must contain a JSON array; existing data was not changed.")
    latest_dates: dict[str, date] = {}
    for index, event in enumerate(events):
        prefix = f"reviews.json event {index + 1}"
        if not isinstance(event, dict):
            raise TrackerError(f"{prefix} must be an object.")
        item_id = nonempty_text(event.get("item_id"), f"{prefix} item_id")
        if item_id not in catalog or item_id != event["item_id"]:
            raise TrackerError(f"{prefix} has unknown item ID {event['item_id']!r}.")
        if event.get("outcome") not in OUTCOMES:
            raise TrackerError(f"{prefix} has an invalid outcome.")
        event_date = parse_date(event.get("date"))
        nonempty_text(event.get("evidence"), f"{prefix} evidence")
        if "assistance" in event and not isinstance(event["assistance"], str):
            raise TrackerError(f"{prefix} assistance must be a string when supplied.")
        if item_id in latest_dates and event_date < latest_dates[item_id]:
            raise TrackerError(f"{prefix} is earlier than the previous event for {item_id}.")
        latest_dates[item_id] = event_date
    return events


def load_events(root: Path, catalog: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    return validate_events(read_json(root / "data" / "reviews.json"), catalog)


def review_states(events: list[dict[str, Any]], as_of: date) -> dict[str, ReviewState]:
    """Derive due dates from completed attempts, never from elapsed time alone."""
    states: dict[str, ReviewState] = {}
    for event in events:
        event_date = parse_date(event["date"])
        if event_date > as_of:
            continue
        item_id = event["item_id"]
        previous = states.get(item_id)
        stage = 0
        due = event_date + timedelta(days=INTERVALS[stage])
        if event["outcome"] == "independent" and previous is not None:
            if event_date >= previous.due:
                stage = min(previous.stage + 1, len(INTERVALS) - 1)
                due = event_date + timedelta(days=INTERVALS[stage])
            else:
                # Early practice is evidence, but has not tested the scheduled gap.
                # Retain the due date so daily retries cannot postpone that review.
                stage = previous.stage
                due = previous.due
        states[item_id] = ReviewState(
            last_date=event_date,
            outcome=event["outcome"],
            stage=stage,
            due=due,
            evidence=event["evidence"],
        )
    return states


def due_items(states: dict[str, ReviewState], as_of: date) -> list[tuple[str, ReviewState]]:
    return sorted(
        ((item_id, state) for item_id, state in states.items() if state.due <= as_of),
        key=lambda item: (item[1].due, item[0]),
    )


def atomic_write(path: Path, content: str) -> None:
    """Replace only after the complete new file has been written and flushed."""
    temp_path: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w", encoding="utf-8", dir=path.parent, prefix=f".{path.name}.",
            suffix=".tmp", delete=False,
        ) as handle:
            temp_path = Path(handle.name)
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_path, path)
        temp_path = None
    finally:
        if temp_path is not None:
            temp_path.unlink(missing_ok=True)


def record_attempt(
    root: Path,
    item_id: str,
    outcome: str,
    event_date: date,
    evidence: str,
    assistance: str | None = None,
    *,
    today: date | None = None,
) -> ReviewState:
    """Append a validated event. The explicit clock argument supports isolated tests."""
    actual_today = today if today is not None else local_today()
    if event_date > actual_today:
        raise TrackerError("Cannot record a future attempt; log the date the work actually happened.")
    evidence = nonempty_text(evidence, "Evidence")
    item_id = nonempty_text(item_id, "Item ID")
    if outcome not in OUTCOMES:
        raise TrackerError(f"Outcome must be one of: {', '.join(OUTCOMES)}.")
    if assistance is not None and not isinstance(assistance, str):
        raise TrackerError("Assistance must be text when supplied.")
    catalog = load_catalog(root)
    if item_id not in catalog:
        raise TrackerError(f"Unknown item ID {item_id!r}; use an ID from data/neetcode150.json or data/topics.json.")
    lock_path = root / "data" / ".reviews.lock"
    try:
        lock_fd = os.open(lock_path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError as exc:
        raise TrackerError("Another recording operation may be running (.reviews.lock exists). No data was changed.") from exc
    try:
        os.close(lock_fd)
        events = load_events(root, catalog)
        event: dict[str, str] = {
            "item_id": item_id, "date": event_date.isoformat(),
            "outcome": outcome, "evidence": evidence,
        }
        if assistance is not None:
            event["assistance"] = assistance.strip()
        updated = events + [event]
        validate_events(updated, catalog)
        # Derive before writing, so even an unrepresentable due date cannot partly succeed.
        states = review_states(updated, actual_today)
        atomic_write(root / "data" / "reviews.json", json.dumps(updated, indent=2, ensure_ascii=False) + "\n")
        return states[item_id]
    finally:
        lock_path.unlink(missing_ok=True)


def status_text(root: Path, as_of: date, limit: int = 5) -> str:
    if limit < 1:
        raise TrackerError("--limit must be at least 1.")
    catalog = load_catalog(root)
    states = review_states(load_events(root, catalog), as_of)
    due = due_items(states, as_of)
    overdue = sum(state.due < as_of for _, state in due)
    lines = [
        f"Study status as of {as_of.isoformat()} (Asia/Kolkata)",
        f"Logged items: {len(states)} / {len(catalog)}. Due: {len(due)} ({overdue} overdue, {len(due) - overdue} today).",
    ]
    if not due:
        lines.append("No reviews due. New practice comes from the daily plan; nothing is automatically marked complete.")
    for item_id, state in due[:limit]:
        label = f"overdue {(as_of - state.due).days}d" if state.due < as_of else "due today"
        lines.append(f"- {item_id}: {catalog[item_id]['title']} | {label} ({state.due}) | latest: {state.outcome}")
    if len(due) > limit:
        lines.append(f"Backlog beyond this {limit}-item display: {len(due) - limit}. Increase --limit to view it; missed reviews remain due.")
    return "\n".join(lines) + "\n"


def markdown_cell(value: Any) -> str:
    # Keep user-entered evidence and catalog labels inside a single table cell.
    return str(value).replace("\\", "\\\\").replace("|", "\\|").replace("\r", " ").replace("\n", " ").replace("<", "&lt;").replace(">", "&gt;")


def dashboard_text(root: Path, as_of: date) -> str:
    catalog = load_catalog(root)
    events = [event for event in load_events(root, catalog) if parse_date(event["date"]) <= as_of]
    states = review_states(events, as_of)
    problem_ids = [item_id for item_id, item in catalog.items() if item["kind"] == "problem"]
    topic_ids = [item_id for item_id, item in catalog.items() if item["kind"] == "topic"]
    problem_set = set(problem_ids)
    helped = {event["item_id"] for event in events if event["item_id"] in problem_set and event["outcome"] in ("learned", "hinted")}
    independent = {event["item_id"] for event in events if event["item_id"] in problem_set and event["outcome"] == "independent"}
    due = due_items(states, as_of)
    lines = [
        "# Preparation progress", "",
        f"As of **{as_of.isoformat()} (Asia/Kolkata)**. Generated from recorded attempts only.", "",
        "An independent attempt is evidence for that item on that date, not a global ability score or a claim of mastery. "
        "Unlogged earlier practice remains unassessed here. Missing a day never completes a review.", "",
        "## Problem learning status", "",
        "Counts below use each problem's **latest** logged outcome.", "",
        "| Status | Problems |", "| --- | ---: |",
        f"| No logged attempt | {sum(item_id not in states for item_id in problem_ids)} |",
    ]
    for outcome in OUTCOMES:
        lines.append(f"| {LABELS[outcome]} | {sum(item_id in states and states[item_id].outcome == outcome for item_id in problem_ids)} |")
    lines.extend([
        f"| **Catalog total** | **{len(problem_ids)}** |", "",
        f"Across the full log: **{len(helped)}** problems studied with explanations or hints; "
        f"**{len(independent)}** problems demonstrated independently at least once. "
        "These groups can overlap; they are not a combined completion count.", "",
        "## Reviews due", "",
        f"**{len(due)}** due or overdue: **{sum(state.due < as_of for _, state in due)}** overdue; "
        f"**{sum(state.due == as_of for _, state in due)}** due today.", "",
    ])
    if due:
        lines.extend(["| ID | Item | Due | Status |", "| --- | --- | --- | --- |"])
        for item_id, state in due:
            label = "Overdue" if state.due < as_of else "Due today"
            lines.append(f"| {markdown_cell(item_id)} | {markdown_cell(catalog[item_id]['title'])} | {state.due} | {label} |")
    else:
        lines.append("No reviews due. Select new work from the daily plan.")
    for heading, item_ids in (("All catalog problems", problem_ids), ("Concepts and other topics", topic_ids)):
        lines.extend(["", f"## {heading}", "", "| ID | Item | Latest outcome | Last attempt | Next review |", "| --- | --- | --- | --- | --- |"])
        for item_id in item_ids:
            state = states.get(item_id)
            cells = [item_id, catalog[item_id]["title"], LABELS[state.outcome] if state else "No logged attempt", state.last_date if state else "—", state.due if state else "—"]
            lines.append("| " + " | ".join(markdown_cell(cell) for cell in cells) + " |")
    lines.extend(["", "## Recent evidence", ""])
    if events:
        lines.extend(["| Date | ID | Outcome | Evidence | Assistance |", "| --- | --- | --- | --- | --- |"])
        # Sort dates for presentation; recording may backfill a different item's history.
        recent = sorted(enumerate(events), key=lambda pair: (pair[1]["date"], pair[0]), reverse=True)[:10]
        for _, event in recent:
            cells = [event["date"], event["item_id"], event["outcome"], event["evidence"], event.get("assistance") or "Not specified"]
            lines.append("| " + " | ".join(markdown_cell(cell) for cell in cells) + " |")
    else:
        lines.append("No attempts recorded yet. The diagnostic and self-reported past practice are not logged as completed learning.")
    lines.extend(["", "Review intervals: 1, 3, 7, 14, then 30 days. Intervals are counted from the actual attempt date. "
                  "An assisted or unsuccessful attempt resets the interval to 1 day. Independent attempts before the scheduled due date "
                  "preserve the current stage and due date; only due or overdue independent reviews advance the interval.", ""])
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    for command in ("status", "today"):
        sub = subparsers.add_parser(command, help="Show due and overdue reviews")
        sub.add_argument("--date", help="As-of date YYYY-MM-DD; defaults to today in Asia/Kolkata")
        sub.add_argument("--limit", type=int, default=5, help="Maximum due items to display (default: 5)")
    record = subparsers.add_parser("record", help="Append evidence for a completed attempt")
    record.add_argument("item_id", help="ID from either catalog")
    record.add_argument("outcome", choices=OUTCOMES)
    record.add_argument("--date", help="Actual attempt date YYYY-MM-DD; defaults to today in Asia/Kolkata")
    record.add_argument("--evidence", required=True, help="Short concrete observation of what happened")
    record.add_argument("--assistance", help="Hints/explanations used, if any")
    dashboard = subparsers.add_parser("dashboard", help="Generate PROGRESS.md from logged evidence")
    dashboard.add_argument("--date", help="As-of date YYYY-MM-DD; defaults to today in Asia/Kolkata")
    return parser


def main(argv: list[str] | None = None, *, root: Path = PROJECT_ROOT) -> int:
    args = build_parser().parse_args(argv)
    try:
        as_of = parse_date(args.date) if args.date else local_today()
        if args.command in ("status", "today"):
            print(status_text(root, as_of, args.limit), end="")
        elif args.command == "record":
            state = record_attempt(root, args.item_id, args.outcome, as_of, args.evidence, args.assistance)
            print(f"Recorded {args.item_id}: {args.outcome} on {as_of}. Next review: {state.due}.")
            print("Run `python3 tools/tracker.py dashboard` to refresh PROGRESS.md.")
        else:
            content = dashboard_text(root, as_of)
            atomic_write(root / "PROGRESS.md", content)
            print(f"Generated PROGRESS.md as of {as_of} from actual recorded attempts.")
    except (TrackerError, OSError, OverflowError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
