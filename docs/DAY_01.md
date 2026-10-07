# Day 1: precise requirements and counting

**Status: planned, not completed.** Budget: 180 minutes within the 24-hour weekly plan. Start whenever the learner has time; the setup date is not a completed study day. This is a guided session, and Day 1 ratings remain unassessed.

## Outcomes

By the end, the learner should be able to describe a function's inputs and numeric output, distinguish an occurrence time from a duration, count repeated values with a map, and test a straightforward implementation against examples. This is a teaching session with a small independent exit check.

## Session sequence

| Time | Activity |
| --- | --- |
| 0–15 min | Retrieval and orientation: identify 2–3 previously studied NeetCode problems if remembered, explain their inputs and outputs, and recall relevant array/set/map operations. Do not require reconstructing all 30 or treat imperfect recall as a Day 1 grade. |
| 15–35 min | Guided specification and count trace: distinguish timestamps from durations, state the fixed-window rule in ordinary language, and trace repeated user IDs being added to and removed from a map. Explain what a set remembers and what it does not. |
| 35–65 min | Fixed-window exercise below: manually mark included events, explain the boundaries, and implement a simple correct function in JavaScript. Derive the implementation before discussing optimization. |
| 65–90 min | Test empty input, repeated users, an event at the left boundary, and an event after the end. Explain expected results before running the code; repair any mismatch between the rule and implementation. |
| 90–105 min | Guided transfer: work a changed input and a changed boundary convention. Explain which condition must change and which parts of the implementation remain valid. Do not introduce a new algorithm just to fill time. |
| 105–150 min | Systems practice: draw the lifecycle of one document job from queued to processing to completed/failed. Locate persistent status, trace a worker crash before and after saving a result, and explain what a replacement worker would need to know. Record unresolved ownership questions for the later lab. |
| 150–170 min | Independent exit check: tutor supplies a fresh fixed-window input and one changed requirement, followed by a short lifecycle trace if time permits. Record prompts and hints; no need for the maximum-across-all-windows problem yet. |
| 170–180 min | Save the learner's code, examples, and actual time; leave Day 1 ratings unassessed and schedule the first recall review. Later independent sessions use the daily rubric. |

This follows the normal allocation of 15 minutes retrieval, 90 minutes DSA, 45 minutes systems/AI, 20 minutes of independent checks, and 10 minutes logging. Pause the active-study clock for breaks; log actual active minutes. Unfinished work stays pending instead of extending the session automatically.

The weekly budget is three core hours daily (21 hours), plus up to 90 flexible minutes on each weekend day (3 hours), for at most 24 hours. Weekend catch-up replaces optional work in those flexible blocks. The 45-minute weekly recap sits inside Sunday's three core hours; it is not an additional session. The planning target is 18 weeks, with a provisional 16–20-week range and progress checked against actual evidence.

## Fixed-window exercise

Events contain an occurrence time, in seconds since logging began, and a user ID. We supply both the duration and the current time.

```js
const events = [
  { timestamp: 101, user: "a" },
  { timestamp: 105, user: "b" },
  { timestamp: 108, user: "a" },
  { timestamp: 110, user: "c" },
];
const durationSeconds = 5;
const currentTimeSeconds = 110;
```

Write `countDistinctUsers(events, durationSeconds, currentTimeSeconds)` in JavaScript.

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
