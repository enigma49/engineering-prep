# Progress reports

Reports guide the next lesson and test whether the learning method is working. They use existing session evidence and review time; they do not add another grading system or extra study hours. Consistency means returning to practice and carrying unfinished work forward. A missed day does not reset completed learning or create a failing score.

## Cadence and budget

| Report | When | Scope and budget |
| --- | --- | --- |
| Session summary | After each actual practice session, including a short or partial session | A brief summary using the existing logging block. Record demonstrated strengths, help, the exact unresolved step, one next action, and due reviews. |
| Weekly report | During the existing weekly recap | Use the 45-minute recap inside core time. Compare actual coverage, retention, help required, and workload; select the next week's priorities. |
| Fortnightly checkpoint | Every two practice weeks | Extend that week's report with comparable independent checks on covered material. Checks replace ordinary practice/exit checks; do not add a second recap or another shift. Revisit the timeline using actual evidence. |
| Broader mock and readiness review | Consider at four-week intervals once enough material is covered | Replace existing practice blocks with an explicitly timed, appropriately scoped mock. If coverage is insufficient, report the gap and use targeted teaching instead. Combine its findings with the fortnightly report. |

The first learning report follows the first actual session. Establish weekly reporting periods from that start and align recaps with the agreed weekly review. Keep lesson order separate from calendar dates. If a reporting period has no new evidence, say so and preserve the last assessment. An absent log means unknown participation, not proof that no study happened. Reports can be produced at the next coaching interaction; this policy does not itself create a scheduled notification.

## Daily summary

Use the session template rather than a duplicate daily file:

1. What was practised and what the learner demonstrated, with an artifact or concrete answer.
2. What was independent, what needed a neutral prompt, directional hint, supplied approach, or language/API help.
3. The exact remaining gap and the next small action.
4. Actual active minutes when known, reviews attempted, backlog carried forward, and next review dates.

Use the task-specific rubric in [ASSESSMENT.md](ASSESSMENT.md). Untested dimensions remain null. Day 1 remains guided and ungraded. Repeating code immediately after instruction is assisted reconstruction, not evidence of delayed retention.

## Weekly and fortnightly reports

Save one report per period as `reports/YYYY-MM-DD-weekly.md` or `reports/YYYY-MM-DD-checkpoint.md`, using [the report template](../reports/TEMPLATE.md). A checkpoint replaces that week's weekly file. Link source sessions, attempts, and artifacts so a reader can check each conclusion.

Include each track below; write **unassessed in this period** where there is no evidence:

| Track | Useful evidence |
| --- | --- |
| Python for DSA | Can implement an already-chosen approach; relevant language/API help and implementation errors. |
| DSA | Requirement interpretation, correctness, implementation, tests and complexity; distinguish familiar recall from unfamiliar transfer. |
| CS fundamentals | Mechanism explanations and small traces or experiments involving networking, databases, operating systems or concurrency. |
| System design | Requirements, coherent data flow, justified decisions, explicit failure/recovery behavior and follow-ups. |
| Applied AI | Pipeline diagnosis, labeled evaluation, metric interpretation, baseline comparisons and measured operational tradeoffs. |
| Labs and project | Acceptance criteria passed, runnable artifacts, reproducible tests/measurements and unresolved defects. |
| Communication and behavioral | Clear explanations, responses to follow-ups, and truthful accounts of personal decisions and outcomes. |

For each track, report the topic covered, evidence and assistance, change since a comparable earlier check, remaining gap, and next action. Avoid assigning a single score to an entire track when only a narrow topic was tested. Do not average unrelated daily scores into a global readiness number.

Report these supporting measures only when the source data exists:

- **Participation and time:** sessions with recorded practice, distinguishing full, short and partial sessions where known; sum known active minutes and explicitly count sessions with unknown time. Use the existing 21-hour core budget and 24-hour ceiling as planning references. Do not infer actual time from planned blocks or missing logs.
- **Independent application:** independent completions out of comparable eligible attempts, with incomplete attempts retained. State difficulty, topics, prior exposure, whether the category was revealed, help, and timing mode. Separate new problems, familiar problems, and reconstruction.
- **Delayed recall:** independent successful scheduled reviews out of scheduled reviews actually attempted. Include hinted and unsuccessful attempts in that denominator, report deferred/overdue items separately, and exclude early retries and immediate reconstruction from this measure. Use the scheduler's existing advancement rules.
- **Transfer:** results on changed requirements or unfamiliar tasks from covered concepts, with the number and scope sampled. State explicitly when transfer has not been checked.
- **Delivery:** which named lab/project acceptance criteria actually pass and which remain open. Document work alone does not establish working implementation.

Prefer counts such as `2 of 3 comparable attempts` over a percentage that hides a small sample. Number of problems encountered and hours spent provide context; neither establishes mastery. A changed difficulty or newly assessed topic is not automatically evidence of regression.

## Decisions the report must produce

- **Continue or advance** when several varied attempts, explanations, relevant tests, and available delayed reviews support it. Keep reviews active after moving on; do not require every hard problem before advancing.
- **Repair a prerequisite** when the same conceptual gap recurs in comparable attempts. Teach a smaller example, then check a changed example. Record the coaching change rather than repeating the same unsuccessful prompt.
- **Practise transfer** when familiar recall succeeds but changed or unfamiliar tasks repeatedly stall. Use variations on covered concepts and reduce new-topic volume until the missing reasoning is clearer.
- **Reduce new material** when recall fails repeatedly or the review queue exceeds its time budget. Cap a normal review queue at five items, explicitly carry the backlog, and use existing core/flex time rather than extending every day.
- **Adjust the forecast** when actual time, retention, or unfinished project criteria differ materially from the plan. Do this after two completed practice weeks and later checkpoints; avoid predicting final ratings.
- **Resume after interruptions** with the next incomplete lesson and priority reviews. Use the 30-minute fallback when useful, then bounded weekend catch-up. Do not restart the curriculum or double the next day's workload to preserve a streak.

Finish each report with a short explanation of what is working, what is not yet established, and no more than three priorities for the next period. If the evidence is too thin for a trend, say so.

## Public record and privacy

Publish sanitized curriculum, practice evidence, assessments and active-study durations within the agreed scope. Keep the personal timetable, private commitments, exact routine/reminder clock times, private reasons for interruptions, and raw conversations out of tracked files and Git history. Reminder settings are managed privately outside this repository. A public report may simply say that work was carried forward, without explaining private circumstances.

Before committing, inspect the diff for both accuracy and privacy. Generate reports from actual participation only; a reminder must never solve, grade, commit or mark practice complete on the learner's behalf.
