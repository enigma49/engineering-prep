# Adaptive practice plan

This plan uses NeetCode 150 as the DSA spine and the existing preparation plan for systems, AI, projects, and interviews. It adds practice structure, not another large curriculum.

**Day 1 is planned, not completed.** No score or completion is inferred from a scheduled date. See [Day 1](DAY_01.md), [baseline](BASELINE.md), and [assessment rules](ASSESSMENT.md).

## Workload and session structure

- **Provisional workload:** 90 minutes Monday–Saturday and 20 minutes on Sunday for recap or rest: at most 9 hours 20 minutes per week. Adjust this after the learner provides their daily schedule.
- No check-in time is chosen and no automation is scheduled. Lesson order and completion remain separate from calendar reminders.
- Reassess after the first week using actual time, fatigue, review backlog, and independent work. Reduce new material before extending sessions.
- The original plan assumed about 24.5 hours per week. Its 15-week duration does not carry over to this workload.
- NeetCode completion is a learning milestone, not proof of mastery. Previously attempted problems can be checked cold; their positions in the list say nothing about current knowledge.

| Full session | Minutes | Purpose |
|---|---:|---|
| Due retrieval | 10 | Attempt scheduled reviews before opening notes |
| DSA learning and practice | 45 | Understand the specification, derive, implement, test |
| Systems or AI focus | 20 | One concept, small experiment, or [lab](LABS.md) step |
| Independent exit check | 10 | A changed example or short fresh task; record help |
| Log and next action | 5 | Save evidence, actual time, and the next review |

Initially the DSA block and exit check account for about 60% of time. The focus block alternates systems and AI. Sunday uses 10 minutes of retrieval, 5 minutes of reflection, and 5 minutes of planning; rest is also valid and is not recorded as completed practice.

Stop at the time limit and log unfinished work. If due reviews exceed their budget, replace some new material with reviews; do not mark unattempted reviews successful.

## First two practice weeks: 14 planned sessions

These are relative slots, not dated claims. D07 and D14 are the Sunday slots in a Monday-start template. If starting midweek, move the next recap to the actual Sunday and keep the full lessons in order. A missed lesson stays pending.

Choose one named NeetCode problem per full session when time allows. If it was previously completed, attempt it cold before deciding whether it needs teaching. The exit check follows the independent/assisted rules in [ASSESSMENT.md](ASSESSMENT.md).

| Slot | DSA or recap work | Systems/AI focus | Evidence to retain |
|---|---|---|---|
| D01 | Guided lesson on plain-language requirements, timestamp ranges, and frequency Maps | A small job-claim example if time permits; otherwise defer | Guided notes only; new assessment scores remain null |
| D02 | Hash-map/set operations and one of Two Sum or Contains Duplicate; include duplicate inputs | Separate retrieval quality from answer quality in a document assistant | Code, tests, and one evaluation question |
| D03 | Derive a correct straightforward solution to a small window-counting task before optimizing | State what a worker must claim atomically | A precise window rule and a trace that could falsify it |
| D04 | Longest Substring Without Repeating Characters: derive the valid-window condition | Define relevant documents, correct answers, and an evaluation baseline | Explain why each state update preserves validity |
| D05 | Revisit timestamp windows; optimize only if the straightforward version is correct | Examine worker crash, retry, and stale ownership | Code plus boundary and repeated-user tests |
| D06 | One mixed, category-hidden easy/medium from covered NeetCode material; no solution preview | Build a tiny held-out evaluation table in the lab | Independent attempt, help level, and failure classification |
| D07 | Sunday recap or rest; review the actual completed week | Adjust workload and queue weak concepts | Short weekly review; pending work remains pending |
| D08 | Valid Palindrome or Two Sum II; justify pointer movement | Distinguish local locking from coordination across replicas | A correctness explanation before code |
| D09 | Group Anagrams or Product of Array Except Self, chosen by the weakest cold check | Calculate and interpret one retrieval metric on tiny examples | Tests and metric numerator/denominator |
| D10 | A fresh small variant of a covered window task; no pattern label supplied | Explain what an idempotency key does and does not guarantee | Separate derivation evidence from familiar-code recall |
| D11 | Binary Search if earlier gates pass; otherwise repair the weakest covered pattern | Trace one AI failure from input through retrieval to answer | Explicit search/window bounds and a failing example |
| D12 | Review one weak NeetCode problem and attempt one short changed example | Compare two system or AI designs using one measurable criterion | Delayed recall result and the reason for the comparison |
| D13 | Cumulative mini-check on covered patterns within the normal session | Brief atomic-ownership and evaluation probes, without notes | Topic-specific independent evidence, not an overall ability score |
| D14 | Sunday recap and checkpoint review, or rest | Choose the next learning block from demonstrated gaps | Keep, repeat, or advance each tested topic |

Do not force an optimization when the straightforward solution is still incorrect. A failed check changes the next lesson; it does not trigger an automatic increase in workload. Untested NeetCode categories remain untested.

## Progression after the first two weeks

Phase boundaries are evidence gates, not promises about completion dates. The original plan's part numbers are retained as a navigation aid.

| Phase | Work and source mapping | Gate before shifting emphasis |
|---|---|---|
| 1: DSA foundations and transfer | Continue NeetCode 150; use original Part 5 for overlap checks. Small systems/AI lessons address the baseline gaps. | Independently interpret, derive, implement, test, and explain several varied problems from covered topics |
| 2: Complete the DSA spine and deepen systems | Finish the chosen NeetCode pass; use Parts 6–8 for OS, concurrency, databases, networks, and distributed systems. Keep Parts 10 and 13 active through small labs. | Delayed recall plus unfamiliar variants work across several patterns; explain an atomic-ownership failure and recovery |
| 3: Integrate design and applied AI | Parts 9–13: general design, AI concepts, estimation, AI design, and practical exercises. Continue mixed DSA and weak-topic repair. | Support design choices with requirements, failure reasoning, measurements, and a small working artifact |
| 4: Interview and project evidence | Parts 14–19: target-role preparation, project explanations, behavior, questions, and resources. Use Parts 20–22 as integration and readiness checklists. | External or rubric-based mocks show repeatable independent performance; unfinished items stay explicit |

Most Part 5 problems overlap NeetCode 150. Do not restart them as if new: check cold, repair weak ones, and use confident repeats for changed or unfamiliar variants. Additional tasks include Accounts Merge, implementing sorting, a rate limiter, and Sliding Window Median; they do not justify a second full DSA curriculum.

As DSA transfer improves, shift the 45-minute main block gradually toward systems/AI labs while preserving coding retrieval and at least two substantive coding sessions per week. Keep the 90-minute ceiling. Follow [LABS.md](LABS.md) for the public project work; a problem count alone is not a portfolio deliverable.

## Review and checkpoint cadence

- Reviews use gaps of **1, 3, 7, 14, then 30 days after the previous successful learning/review event**. These are growing gaps, not offsets from the first attempt. After the final step, continue 30-day maintenance when useful.
- Initial teaching may create a next-day review; it is not an independent pass. An incorrect or hinted review resets the item to a next-day review. Advance the interval only on an independent success on or after its due date. Early retries preserve the original due date and stage.
- Use the actual completion timestamp when recording a review. A late review advances from its real successful date; missed dates do not create fictional attempts.
- Every 7 days after the first completed session, review completed work, backlog, and time spent. No completed work means a scheduling check, not a learning score.
- At 14 days, review cumulative evidence from the actual lessons. If coverage is too thin, record that and continue the unfinished block.
- After 28 days, run a balanced mock only if there is enough independent coding, systems, and AI evidence to make it useful. Otherwise use the session to repair the weakest foundation and record why the mock was deferred.

The [tracker](../tools/tracker.py) records actual attempts and due reviews. [README](../README.md) explains the repository workflow. Scores describe demonstrated work at a point in time; they are not a fixed estimate of ability.
