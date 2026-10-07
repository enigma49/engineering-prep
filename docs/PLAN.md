# Adaptive practice plan

This plan uses NeetCode 150 as the DSA spine and the existing preparation plan for systems, AI, projects, and interviews. It adds practice structure, not another large curriculum.

**Day 1 is planned, not completed.** No score or completion is inferred from a scheduled date. See [Day 1](DAY_01.md), [baseline](BASELINE.md), and [assessment rules](ASSESSMENT.md).

## Workload and session structure

- **Agreed weekly capacity:** up to 24 hours. Three hours each day gives 21 hours; add up to 90 minutes on Saturday and 90 minutes on Sunday to reach 24. This is a provisional distribution of the learner's chosen weekly budget; exact clock times await their detailed schedule.
- Plan **21 hours of core work plus three hours of weekend flexibility**. The weekly 45-minute recap is included in Sunday's three core hours. Flexibility is used for catch-up first, then optional review or project extensions. Do not make essential new work depend on both the full core allocation and the same hours being available again for catch-up.
- No check-in time is chosen and no automation is scheduled. Lesson order and completion remain separate from calendar reminders.
- Reassess after the first week using actual time, fatigue, review backlog, and independent work. Reduce new material before extending sessions.
- The original plan assumed about 24.5 hours per week, now close to the agreed capacity. Use the 18-week target below to include consolidation and one project; do not treat the original 15-week calendar as a guaranteed outcome.
- NeetCode completion is a learning milestone, not proof of mastery. Previously attempted problems can be checked cold; their positions in the list say nothing about current knowledge.

| Normal weekday session | Minutes | Purpose |
|---|---:|---|
| Due retrieval | 15 | Attempt scheduled reviews before opening notes |
| DSA learning and practice | 90 | Understand the specification, derive, implement, test |
| Systems or AI focus | 45 | One concept, experiment, or [lab](LABS.md) step |
| Independent exit check | 20 | A changed example or short fresh task; record help |
| Log and next action | 10 | Save evidence, actual time, and the next review |

Initially the DSA block and exit check account for about 60% of a normal session. The focus block alternates systems and AI. Sessions may be split across the day. Breaks and setup are not logged as active practice. On Saturday use core time for consolidation and a longer lab or project block. On Sunday use 45 core minutes for recap/checkpoint and the remaining 135 core minutes for due reviews, weak-topic repair, or the current lab/project.

**Missed-day rule:** carry the lesson forward and use weekend flexibility before optional new work. Missing one three-hour weekday and using all three flex hours can preserve the 21-hour core plan, but actual study that week is then 21 hours, not 24. Missing more time means carrying some work into the next week. Do not manufacture completed hours or require an unplanned marathon to preserve dates.

Stop at the chosen time limit and log unfinished work. If due reviews exceed their budget, replace some new material with reviews; do not mark unattempted reviews successful. The 30-minute busy-day fallback remains available. Recalculate the forecast if actual weekly time or retention differs materially from the plan.

## Language

Use **JavaScript** for all learner DSA solutions, coding exercises, and project code, with **Node.js** for local execution. Teach `Map` and `Set`, reference versus value behavior, numeric sorting, strings, recursion, integer limits, and suitable queue/heap implementations when a task needs them. Cover promises, the event loop, cancellation, and bounded concurrency in the systems/project track. Language details support the problem being studied rather than becoming another prerequisite course.

The existing Python tracker is assistant-operated tooling. The learner does not need to learn Python to follow this plan.

## Provisional timeline and topic scope

**Working target: 18 weeks, with a 16–20-week planning range (roughly four to five months)** at up to 24 hours per week. This replaces the earlier 36–44-week estimate based on 9 hours 20 minutes per week. It is a capacity estimate, not a measured prediction of learning speed or a guaranteed upper bound. The original plan budgeted 15 × 24.5 = 367.5 hours; the same hours take about 15.3 weeks at 24 hours. Eighteen weeks provides 378 core hours and up to 432 hours including flexibility. Prior knowledge and overlap may save time; retention and project work may need more. Re-estimate after two completed practice weeks and at later checkpoints.

The table gives emphasis windows within an 18-week model. Topics overlap, and demonstrated readiness can move them earlier or later. Weeks 19–20 are a reserve for weak topics or unfinished project work. The first 14 sessions below remain the concrete starting plan with the expanded time budget. Interview practice begins earlier in small doses; applications can begin when relevant readiness checks pass.

| Approximate weeks | Main emphasis | Evidence we want |
| --- | --- | --- |
| 1–2 | Requirements, correct straightforward solutions, JavaScript arrays/maps/sets, frequency counting, boundaries, and window reasoning. Job lifecycle and RAG diagnosis alongside. | Correct explanations and implementations on covered tasks, changed examples and duplicates; identify which prior NeetCode work is retained. |
| 3–7 | Two pointers, sliding windows, stacks, binary search, linked lists, recursion, trees, and heaps. OS/concurrency, networking, databases. Build the worker-recovery lab, then the evaluation lab. | Increasingly independent easy/medium attempts, delayed recall, and reproducible lab failure tests and metric calculations. |
| 8–12 | Graphs, backtracking, tries, intervals, greedy methods, dynamic programming, and remaining NeetCode categories. Distributed systems, general design, applied AI, capacity estimation. Begin one integrated project when the labs are ready. | Broader DSA coverage, fresh mixed attempts, complete design discussions, and a working project slice with tests. |
| 13–16 | Complete or repair the NeetCode pass, practice mixed unseen problems and design follow-ups, and finish and measure the project. | Retained skills across patterns, defensible design tradeoffs, and a runnable project with reproducible measurements. |
| 17–18, with reserve through 20 | Targeted mocks, uncovered/weak-topic repair, project polish, project explanations, behavioral stories, and role-specific preparation. | Repeatable independent performance and one finished, explainable showcase project; explicit remaining gaps. |

Finishing the selected NeetCode pass remains a goal across these stages. These dates do not guarantee all 150 problems are independently mastered. Do not sacrifice retention or silently mark a difficult problem complete to keep the calendar.

Topic coverage beyond DSA:

- **CS and systems foundations:** processes/threads, concurrency and atomic operations, networking (DNS, HTTP, TCP, TLS), database indexes and transactions, isolation, connection pools, and basic API/object design.
- **System design:** requirements, capacity estimates, data models, caches, queues, retries, idempotency, ownership/leases, replication, partitioning, consistency, backpressure, observability, and recovery. Practice concrete services such as a rate limiter, job processor, notification service, and document-processing platform.
- **Applied AI:** tokens and context, embeddings, attention/KV-cache intuition, structured outputs, streaming, tool calls, chunking, dense/sparse/hybrid retrieval, reranking, source freshness, retrieval and answer evaluation, held-out cases, grounding, abstention, cost/latency, provider routing, bounded workflows, and access/security failure cases. Introduce basic sampling, leakage, and train/validation/test concepts through evaluation. Fine-tuning and GPU serving start at a conceptual level; deep model training or research requires a separate later track.
- **Interview communication:** deriving an approach aloud, explaining tradeoffs, following failures through a design, project deep dives, and accurate stories about ownership, incidents, decisions, collaboration, and impact. Use actual experience; never invent metrics.

Initially reserve **3–4 hours per week for hands-on labs within the systems/AI allocation**. Once the labs are ready, allocate **six core hours weekly to the showcase project in weeks 9–16**, replacing some new-topic time; reserve about four hours weekly for project polish in weeks 17–18. These hours are inside the 21 core hours, not additions to the 24-hour ceiling or promises to spend catch-up time twice. Keep at least two substantive coding sessions and due reviews in every project-heavy week. Target **one polished project plus two focused labs**. Choose an evaluated document assistant or a reliable LLM gateway, then finish it before considering a second showcase project. See [LABS.md](LABS.md) for acceptance criteria.

Expected outcome is stronger independent problem solving and practical AI/backend engineering evidence. Unseen-medium performance must be demonstrated on multiple mixed tasks; selected hard problems are a stretch goal. A completed calendar, problem count, or predicted `/10` rating is not evidence of top-company readiness. Use the [assessment rules](ASSESSMENT.md) and appropriately scoped mocks to make that decision.

## First two practice weeks: 14 planned sessions

These are relative slots, not dated claims. D07 and D14 are the Sunday slots in a Monday-start template, including 45 minutes of recap within that day's core budget and remaining time for consolidation or lab work. If starting midweek, move the next recap to the actual Sunday and keep the full lessons in order. Saturday and Sunday each have up to 90 additional flex minutes. A missed lesson stays pending.

Choose one main NeetCode problem or foundation exercise per session initially. If time remains after a correct explanation, implementation, and tests, use a changed example or a second appropriately sized problem. Do not force a daily problem quota. Previously completed problems get a cold attempt before teaching. The exit check follows the independent/assisted rules in [ASSESSMENT.md](ASSESSMENT.md).

| Slot | DSA or recap work | Systems/AI focus | Evidence to retain |
|---|---|---|---|
| D01 | Guided lesson on plain-language requirements, timestamp ranges, frequency Maps, and tested JavaScript code | Job lifecycle and one failure trace | Guided notes and exit evidence; new assessment scores remain null |
| D02 | Hash-map/set operations and one of Two Sum or Contains Duplicate; include duplicate inputs | Separate retrieval quality from answer quality in a document assistant | Code, tests, and one evaluation question |
| D03 | Derive a correct straightforward solution to a small window-counting task before optimizing | State what a worker must claim atomically | A precise window rule and a trace that could falsify it |
| D04 | Longest Substring Without Repeating Characters: derive the valid-window condition | Define relevant documents, correct answers, and an evaluation baseline | Explain why each state update preserves validity |
| D05 | Revisit timestamp windows; optimize only if the straightforward version is correct | Examine worker crash, retry, and stale ownership | Code plus boundary and repeated-user tests |
| D06 | One mixed, category-hidden easy/medium from covered NeetCode material; no solution preview | Build a tiny held-out evaluation table in the lab | Independent attempt, help level, and failure classification |
| D07 | 45-minute recap of the actual completed week; use remaining core time for recall and weak-topic repair | Continue the current lab and adjust workload | Weekly review; pending work remains pending |
| D08 | Valid Palindrome or Two Sum II; justify pointer movement | Distinguish local locking from coordination across replicas | A correctness explanation before code |
| D09 | Group Anagrams or Product of Array Except Self, chosen by the weakest cold check | Calculate and interpret one retrieval metric on tiny examples | Tests and metric numerator/denominator |
| D10 | A fresh small variant of a covered window task; no pattern label supplied | Explain what an idempotency key does and does not guarantee | Separate derivation evidence from familiar-code recall |
| D11 | Binary Search if earlier gates pass; otherwise repair the weakest covered pattern | Trace one AI failure from input through retrieval to answer | Explicit search/window bounds and a failing example |
| D12 | Review one weak NeetCode problem and attempt one short changed example | Compare two system or AI designs using one measurable criterion | Delayed recall result and the reason for the comparison |
| D13 | Cumulative mini-check on covered patterns within the normal session | Brief atomic-ownership and evaluation probes, without notes | Topic-specific independent evidence, not an overall ability score |
| D14 | 45-minute recap/checkpoint; consolidate covered material in remaining core time | Choose the next block from demonstrated gaps; continue the lab | Keep, repeat, or advance each tested topic |

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

As DSA transfer improves, reallocate some main practice blocks to systems/AI projects using the weekly allocation above, while preserving coding retrieval and at least two substantive coding sessions per week. Keep the agreed three-hour normal session and 24-hour weekly ceiling, with the stated weekend flexibility. Follow [LABS.md](LABS.md) for public project work; a problem count alone is not a portfolio deliverable.

## Review and checkpoint cadence

- Reviews use gaps of **1, 3, 7, 14, then 30 days after the previous successful learning/review event**. These are growing gaps, not offsets from the first attempt. After the final step, continue 30-day maintenance when useful.
- Initial teaching may create a next-day review; it is not an independent pass. An incorrect or hinted review resets the item to a next-day review. Advance the interval only on an independent success on or after its due date. Early retries preserve the original due date and stage.
- Use the actual completion timestamp when recording a review. A late review advances from its real successful date; missed dates do not create fictional attempts.
- Every 7 days after the first completed session, review completed work, backlog, and time spent. No completed work means a scheduling check, not a learning score.
- At 14 days, review cumulative evidence from the actual lessons. If coverage is too thin, record that and continue the unfinished block.
- After 28 days, run a balanced mock only if there is enough independent coding, systems, and AI evidence to make it useful. Otherwise use the session to repair the weakest foundation and record why the mock was deferred.

The [tracker](../tools/tracker.py) records actual attempts and due reviews. [README](../README.md) explains the repository workflow. Scores describe demonstrated work at a point in time; they are not a fixed estimate of ability.
