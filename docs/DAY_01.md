# Day 1: JavaScript collections and reasoning

**Status: in progress, not completed.** See [the current session](../sessions/2026-10-13-D01.md). Budget: 180 minutes within the 24-hour weekly plan. The learner chose JavaScript during this session. This is guided learning, and Day 1 ratings remain unassessed (`null`).

## Outcomes

By the end, the learner should be able to describe a function's inputs and numeric output, distinguish an array's index from its value, explain what a JavaScript `Set` and `Map` represent, trace repeated values, and test a straightforward implementation against examples. This is the learner's first formal DSA study program: teach unfamiliar concepts before expecting an independent solution. It is a guided session with a small independent exit check.

## Session sequence

| Time | Activity |
| --- | --- |
| 0–15 min | Retrieval and orientation: acknowledge the 27 previously studied problems whose titles are now identified across Arrays & Hashing, Two Pointers, Stack, and Sliding Window. Choose one familiar task or collection concept for a low-pressure explanation. Do not require reconstructing the list or treat prior study as established mastery. No prior review is due merely because the titles were imported. |
| 15–35 min | JavaScript orientation only where needed: function inputs and return values, arrays, indices versus values, `for...of`, array `.length`, and collection `.size`. Explain unfamiliar terms using small examples; use demonstrated familiarity to move directly into reasoning or practice. |
| 35–65 min | Teach what a `Set` remembers and what a `Map` can associate with each key where needed. Trace a short array with repeated values and a small frequency table by hand. Clarify the array exercise below, obtain the learner's approach before suggesting a structure, and begin their JavaScript implementation. Introduce operations when their purpose is understood. |
| 65–90 min | Complete and test the straightforward implementation. Cover empty input, one item, all repeated users, and all different users. State expected results before running code; repair any difference between the requirement and behavior. Save the learner's own work. |
| 90–105 min | Guided reasoning: trace the code on changed input and count visits or comparisons for a small array. Only if this is comfortable, introduce input size and basic time/space growth in plain language, followed by simple Big-O notation. Do not require formal complexity analysis before its meaning is taught. |
| 105–150 min | Systems practice: build on the earlier useful queue, retry, and recovery ideas by drawing one document job's queued/processing/completed/failed lifecycle. Teach or clarify persistent status, then trace a worker crash before or after saving a result. Ask what a replacement worker needs to know. Precise lifecycle and ownership reasoning remain incompletely assessed; record open questions for the later lab without assigning a score today. |
| 150–170 min | Independent exit check: supply a fresh short user array without an answer and ask for the required result and a trace or reconstruction of the function. Include a repeated-value or empty-input case. Record any prompts or hints and distinguish immediate reconstruction from delayed recall. Use a short lifecycle explanation only if time permits. |
| 170–180 min | Save the learner's code, examples, assistance, and actual time; leave Day 1 ratings unassessed (`null`). Schedule recall only for material actually practised. Later independent sessions use the daily rubric. |

This follows the normal allocation of 15 minutes retrieval, 90 minutes DSA, 45 minutes systems/AI, 20 minutes of independent checks, and 10 minutes logging. Pause the active-study clock for breaks; log actual active minutes. Unfinished work stays pending instead of extending the session automatically.

Record JavaScript syntax or API help separately from algorithmic help. Clarifying the stated input or return type is neutral clarification; recommending the collection that solves the task can be directional help. A generic `Map` access example need not supply the algorithm, but its effect on implementation independence must still be recorded. Use Node.js for execution. The Python progress utility is assistant-maintained and is not a learner prerequisite.

The weekly budget is three core hours daily (21 hours), plus up to 90 flexible minutes on each weekend day (3 hours), for at most 24 hours. Weekend catch-up replaces optional work in those flexible blocks. The 45-minute weekly recap sits inside Sunday's three core hours; it is not an additional session. The planning target is 18 weeks, with a provisional 16–20-week range and progress checked against actual evidence.

## Array exercise

The input `users` is an array of user IDs, represented by strings. Each array entry records one occurrence of a user; the same user can appear more than once. For example:

```javascript
const users = ["a", "b", "a", "c", "b"];
```

Write `countDistinctUsers(users)` in JavaScript. Return the **number of different user IDs**, as a whole-number `number` value. Count a repeated user only once. Empty input returns `0`. There are no timestamps, time units, or window boundaries in this exercise.

First explain the expected result for the supplied example in ordinary language. The tutor should wait for the learner's explanation and approach before suggesting implementation details. Save the learner's own work under `practice/dsa/`; do not prefill the answer or a reference solution.

## Exit evidence

- Can the learner explain the input, the required output, and the meaning of "different" using the supplied array?
- Can the learner distinguish an array position from the value at that position?
- Does the returned value have the required type?
- Can the learner explain what the selected collection remembers, including how repeated values behave?
- Does the code match the stated rule on changed, repeated-value, and empty inputs?
- If operation counting was taught, can the learner trace the work on a small input? Leave complexity unassessed if it was not covered.
- Which parts were taught, prompted, or independently demonstrated?
- Which help concerned JavaScript syntax/APIs, and which concerned the algorithm or requirements?

Keep timestamps and window membership for a later lesson, after basic collections and straightforward counting are secure. If this material is already easy, use a small frequency-counting variation or deepen the explanation of operation counts. Do not introduce a moving-window algorithm just to fill the session.

## Busy-day version: 30 minutes

Use 5 minutes for due recall, 15 minutes for one manual example and implementation step, 5 minutes for a changed example, and 5 minutes for logging. Carry unfinished work forward explicitly.
