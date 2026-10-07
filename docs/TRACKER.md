# Evidence and review tracker

The tracker uses Python 3.9 or newer and the standard library. Run commands from the repository root. It schedules recorded work; it does not solve problems, grade answers, select new lessons, or produce a global ability rating.

```sh
python3 tools/tracker.py today
python3 tools/tracker.py status --date 2026-10-08 --limit 10
```

`today` and `status` are aliases. Dates default to the current date in **Asia/Kolkata**. The default display shows at most five due items, oldest first, and reports the remaining backlog. Missed days leave reviews overdue. An empty queue does not mean the curriculum is complete; select new work from the daily plan.

## Record completed practice

Use a problem ID from `data/neetcode150.json` or a concept ID from `data/topics.json`.

```sh
python3 tools/tracker.py record nc-001 learned \
  --evidence "Understood set membership after an explanation; not yet reproduced independently." \
  --assistance "Read the worked solution."

python3 tools/tracker.py record dsa.requirements independent \
  --evidence "Restated the inputs and output and produced correct boundary examples without hints."
```

These are syntax examples, not instructions to claim work that has not happened. Use your actual outcome and evidence. Add `--date YYYY-MM-DD` to record an earlier attempt. Future attempts are rejected. Historical entries must be appended in nondecreasing date order **for that item**; another item's earlier history can be added independently.

| Outcome | When to use it |
| --- | --- |
| `learned` | Studied an explanation or demonstration; independent reproduction is not yet demonstrated. |
| `independent` | Completed this attempt without solution guidance and explained/tested the reasoning. This is item-specific evidence, not a mastery claim. |
| `hinted` | Made an attempt that needed a hint or other solution guidance. Record the assistance. |
| `needs_review` | The attempt exposed an unresolved error or gap. |

Evidence is required. Describe what was actually demonstrated, the failed case, or the missing step. A count of problems viewed is not evidence of independent performance. The tracker records the outcome supplied by the learner or coach; it does not verify it automatically.

The repository is public. Keep evidence about concepts, attempts, and results. Do not include personal documents, employer/customer data, credentials, or private interview transcripts.

## Spaced reviews

The intervals are **1, 3, 7, 14, and 30 days**. They support a recall routine; they are not a guarantee of retention.

- A first attempt schedules a review one day later, including a first independent attempt.
- An independent review on or after its scheduled due date advances one stage, up to 30 days.
- `learned`, `hinted`, and `needs_review` reset the interval to one day.
- Independent attempts before the scheduled due date, including same-day retries, are saved but do not advance the stage or change the existing due date. Early practice does not count as demonstrating retention across the scheduled gap.
- The next review is calculated from the actual attempt date. Waiting longer never advances the stage automatically.

For example: an explanation on October 7 schedules October 8. An independent review on October 8 schedules October 11. Extra independent practice on October 9 or 10 keeps the October 11 review and the same stage. If that scheduled review actually happens on October 13, a successful independent attempt schedules October 20. A hinted attempt instead schedules October 14.

`--date` on `status` or `dashboard` is an as-of view and can inspect future due dates. It cannot record future learning. A historical view ignores attempts after its selected date.

## Refresh the public dashboard

```sh
python3 tools/tracker.py dashboard
```

This generates `PROGRESS.md` from actual log entries and lists every catalog problem and concept. It separates the latest outcome from the overlapping historical counts of problems studied with help and problems demonstrated independently. Self-reported past practice and the initial diagnostic are not automatically marked complete. No interview-readiness percentage or global skill score is computed.

Recording an attempt does not regenerate the dashboard automatically. Refresh it after the session, review the diff, and then commit the files when appropriate. The CLI never runs Git or contacts GitHub.

## Data and recovery

`data/reviews.json` is an append-only JSON array. Each event has this shape:

```json
{
  "item_id": "nc-001",
  "date": "2026-10-07",
  "outcome": "learned",
  "evidence": "Concrete observation of the attempt.",
  "assistance": "Optional description of help used."
}
```

The JSON array is atomically replaced after appending a validated event. Earlier events are retained. Invalid JSON, unknown IDs, missing evidence, invalid outcomes, and out-of-order dates cause the operation to fail without overwriting the log. Back up or inspect a corrupt file and restore a known-good version before retrying; the CLI never resets it silently.

A short-lived `data/.reviews.lock` protects against concurrent record commands. If a process is killed and leaves that file behind, first confirm no recording process is running, then remove the stale lock and retry. A leftover temporary file after a hard process termination is not the log; inspect it separately before cleanup. Atomic replacement prevents a partial new file from replacing the previous log, but it is not a backup against disk loss.

Tests create their own temporary repository fixtures and never modify the real learning log:

```sh
python3 -m unittest discover -s tests -v
```

The Python functions accept a repository root and test clock for isolated tests. The user-facing CLI deliberately has no path option: its data files and generated dashboard stay in this repository.
