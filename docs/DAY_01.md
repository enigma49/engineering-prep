# Day 1: precise requirements and counting

**Status: planned, not completed.** Provisional budget: 90 minutes. Start whenever the learner has time; the setup date is not a completed study day.

## Outcomes

By the end, the learner should be able to describe a function's inputs and numeric output, distinguish an occurrence time from a duration, count repeated values with a map, and test a straightforward implementation against examples. This is a teaching session with a small independent exit check.

## Session sequence

| Time | Activity |
| --- | --- |
| 0–10 min | Explain the task in ordinary language; identify 2–3 previously studied NeetCode problems if remembered. Do not require reconstructing all 30. |
| 10–25 min | Guided arrays/set/map exercise: trace counts as repeated user IDs are added and removed. Explain what a set remembers and what it does not. |
| 25–45 min | Fixed-window exercise below: manually work examples, state the inclusion condition, and implement a simple correct function. |
| 45–55 min | Test empty input, repeated users, an event at the left boundary, and an event after the end. Explain the result before running code. |
| 55–75 min | Systems micro-lesson: draw the lifecycle of one document job from queued to processing to completed/failed. Locate where status persists if a worker dies. |
| 75–85 min | Independent exit check: tutor supplies a new fixed-window input and one changed requirement. Record any hints; no need for the maximum-across-all-windows problem yet. |
| 85–90 min | Save evidence, leave Day 1 ratings unassessed, and schedule the first recall review. Later independent sessions use the daily rubric. |

## Fixed-window exercise

Events contain an occurrence time, in seconds since logging began, and a user ID. We supply both the duration and the current time.

```text
events = [(101, "a"), (105, "b"), (108, "a"), (110, "c")]
durationSeconds = 5
currentTimeSeconds = 110
```

Write `countDistinctUsers(events, durationSeconds, currentTimeSeconds)`.

Include an event if its time is strictly greater than `currentTimeSeconds - durationSeconds` and at most `currentTimeSeconds`. Return the number of different user IDs in that interval. Empty input returns 0. Events after the current time do not count.

First mark the included events by hand and explain the units. The tutor should wait for that explanation before discussing implementation. A simple loop is sufficient. Save the learner's own work under `practice/dsa/`; do not prefill a reference solution.

## Exit evidence

- Can the learner state the inclusion rule using the example's actual numbers?
- Does the returned value have the required type?
- Can the learner explain duplicates and both boundaries?
- Does the code match the stated rule on a new example?
- Which parts were taught, prompted, or independently demonstrated?

Do not require an optimized moving-window algorithm today. Introduce that only once fixed-window reasoning is secure. If this material is already easy, move to an unfamiliar variation instead of extending repetitive explanation.

## Busy-day version: 30 minutes

Use 5 minutes for due recall, 15 minutes for one manual example and implementation step, 5 minutes for a changed example, and 5 minutes for logging. Carry unfinished work forward explicitly.
