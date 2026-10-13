# Adaptive practice plan

This plan uses NeetCode 150 as the DSA spine and the existing preparation plan for systems, AI, projects, and interviews. It adds practice structure, not another large curriculum.

**Day 1 is planned, not completed.** No score or completion is inferred from a scheduled date. See [Day 1](DAY_01.md), [baseline](BASELINE.md), and [assessment rules](ASSESSMENT.md).

## Foundations-first starting point

This is the learner's first formal DSA study. They have identified 27 previously studied problems across Arrays & Hashing, Two Pointers, Stack, and Sliding Window, but report limited conceptual understanding. See [prior practice](../data/prior_practice.json). Do not assume the underlying theory was learned just because a problem was encountered, and do not discard the familiarity they already have.

For each new topic, teach what it represents, its basic operations, a small manual trace, and the rule that makes the approach correct. Begin with Python lists, indices, sets, dictionaries, loops, and simple counting. Introduce time and extra-space complexity by counting work on small inputs before using Big O notation. Explain terms such as hash map, invariant, recursion, and amortized cost when they arise rather than treating them as prerequisites the learner already knows.

Use **concept explanation → tiny guided exercise → appropriately scoped independent attempt → feedback → delayed review**. An initial ungraded check can reveal familiar material and reduce repetition. The timed problem protocol applies when the relevant concept has been introduced and the learner can trace a basic example. A topic that still lacks prerequisites receives teaching, not a surprise interview test.

The first two weeks now emphasize foundations and Arrays & Hashing. Move into pointers and other branches only when the small checks support it. Existing software-engineering experience can still support systems and AI work; the DSA clarification does not reset every domain to zero. Keep the 18-week target as a capacity forecast and revisit it after two weeks of actual learning evidence; it is not a deadline for claiming readiness.

## Workload and session structure

- **Agreed weekly capacity:** up to 24 hours. Three hours each day gives 21 hours; add up to 90 minutes on Saturday and 90 minutes on Sunday to reach 24. This is a provisional distribution of the learner's chosen weekly budget; personal clock times are managed privately outside the repository.
- Plan **21 hours of core work plus three hours of weekend flexibility**. The weekly 45-minute recap is included in Sunday's three core hours. Flexibility is used for catch-up first, then optional review or project extensions. Do not make essential new work depend on both the full core allocation and the same hours being available again for catch-up.
- Reminder settings are managed privately outside this repository. Lesson order and completion remain separate from calendar reminders.
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

Use **Python 3 for DSA**. The learner reports some basic Python knowledge and wants to build fluency through problem solving. This supersedes the earlier JavaScript choice. Prior familiarity is self-reported and will be checked through small exercises; it is not a completed Python course or an assessment score.

During the **first five sessions**, use up to **20 minutes of the existing 90-minute DSA block** for Python orientation when needed. Start with functions, indentation, loops, `range`, lists, dictionaries, sets, membership, `len`, and simple tests. Add iteration helpers, sorting, mutability, strings, and recursion as problems require them. Introduce `collections.Counter`, `defaultdict`, `deque`, and `heapq` at the relevant topics, after the learner understands the behavior being represented. Reduce orientation when a cold check shows fluency; do not delay all DSA work until a separate language course is finished.

Use a short syntax reference during learning practice and disclose its use. Distinguish a Python API lookup from a hint that supplies an algorithm; both must be recorded accurately. Implementation mistakes still need correction, while demonstrated reasoning is assessed on its own evidence. See [ASSESSMENT.md](ASSESSMENT.md). Day 1 remains guided and ungraded. Reassess language friction and the overall pace after two weeks; the 18-week target remains provisional.

Node.js remains the provisional runtime for portfolio projects. Select each project's implementation language when its build begins; switching DSA to Python does not automatically change the project stack. The existing Python progress utility remains assistant-maintained so studying its implementation is optional.

## How to practise each DSA problem

Use a bounded independent attempt followed by teaching and reconstruction. Learning a new concept and assessing independent performance are different activities. A wholly unfamiliar concept can receive a short explanation first; label the subsequent practice accordingly. Day 1 retains its guided schedule and null ratings.

Once a task is suitable for an independent attempt, this is the default allocation inside the existing 90-minute DSA block:

| Activity | Minutes | Evidence |
| --- | --- | --- |
| Independent attempt after the statement is clear | 25 | Save the approach, current code, tested examples, and exact sticking point at the deadline. |
| Examine the initial attempt | 10 | Identify correct reasoning and the first unresolved requirement, concept, implementation step, or test. |
| Hints, explanation, and tracing | 35 | Use the smallest useful hint first; explain the complete approach when needed and trace why it works. |
| Reconstruct and test with the explanation closed | 20 | Write the code from a blank file, check boundaries, and explain correctness and complexity. This remains assisted learning if the approach was supplied. |

These are adjustable learning budgets, not employer thresholds. Python orientation and requirement clarification must fit inside the 90 minutes; shorten or reallocate other portions as needed rather than adding time. During learning practice, 15–20 minutes without meaningful progress is a reason to request help earlier, not to spend the rest of the day stuck. If the explanation is still unclear, use a smaller prerequisite exercise and carry the original problem forward.

Record the initial attempt before giving a strategy. When the timer ends, partial work is assessed on what it demonstrates; an unfinished optimization does not erase a correct straightforward solution. Any further independent time is recorded separately rather than extending the original deadline silently. Do not label work completed after a hint as an independent solve.

To check understanding after an explanation, ask the learner to state the rule the algorithm maintains, trace a different input, explain why state changes are safe, and justify time and space costs. A successful immediate reconstruction does not establish delayed retention. Schedule the later review using the existing growing-gap policy and use changed or unfamiliar examples to test transfer.

Initially learn related problems together along the roadmap. Once several topics are covered, include **mixed checks without category labels**, drawn from those topics, within weekly or fortnightly review time. Seeing a topic label during learning is useful context, but does not show that the learner identified the pattern independently. Earlier practice reportedly used NeetCode 150; do not assume it was random or infer why it failed to transfer without checking the actual topics and attempts.

The eventual speed target is **many representative unseen medium problems completed independently in 20–30 minutes**, including interpretation, implementation, tests, and a correctness/complexity explanation. Measure this on a series of mixed problems across topics and record incomplete attempts as well as successes. It is an aspiration to work toward, not an entry requirement or a promise for every problem. Formal interview-style rounds may use 35–45 minutes and include follow-ups; set their format and timing before starting. See [ASSESSMENT.md](ASSESSMENT.md) for timing and assistance records.

## DSA topic order

Follow the [NeetCode roadmap](https://neetcode.io/roadmap) shared by the learner as the default progression through NeetCode 150. The following groups reflect its branches, with one main new topic selected at a time. Earlier topics remain in the review queue. This orders the existing curriculum; it does not add another problem list or another study block.

| Roadmap group | Topics |
| --- | --- |
| 1 | Arrays & Hashing, using Python lists, dictionaries, and sets |
| 2 | Two Pointers and Stack |
| 3 | Binary Search, Sliding Window, and Linked List |
| 4 | Trees, including explicit recursion and call-stack practice |
| 5 | Tries, Heap / Priority Queue, and Backtracking |
| 6 | Intervals and Greedy on the heap branch; Graphs and 1-D Dynamic Programming on the backtracking branch |
| 7 | Advanced Graphs, 2-D Dynamic Programming, and Bit Manipulation |
| 8 | Math & Geometry |

These are suggested learning connections, not universal prerequisite claims. Basic intervals need not wait for heap mastery; graph traversal need not wait for every backtracking problem; DP should build on state definitions, recurrences, and repeated subproblems. Choose a sensible order within a group based on the learner's demonstrated understanding and the actual problem's requirements.

Before shifting the main topic, seek a few varied independent attempts (initially about 2–3 appropriately scoped tasks), clear explanations, and relevant edge-case tests. This is an adjustable coaching check, not proof of mastery. Continue delayed recall and unfamiliar variants after advancing. Do not require every problem, especially every hard, to be solved before starting the next topic. Preserve incomplete items for later repair.

Day 1 uses a plain list of user IDs to teach requirements and Python collections. Introduce fixed-interval filtering later as a small boundary exercise; introduce moving/sliding-window state after arrays/hashing and basic pointer reasoning are secure.

## Provisional timeline and topic scope

**Working target: 18 weeks, with a 16–20-week planning range (roughly four to five months)** at up to 24 hours per week. This replaces the earlier 36–44-week estimate based on 9 hours 20 minutes per week. It is a capacity estimate, not a measured prediction of learning speed or a guaranteed upper bound. The original plan budgeted 15 × 24.5 = 367.5 hours; the same hours take about 15.3 weeks at 24 hours. Eighteen weeks provides 378 core hours and up to 432 hours including flexibility. Prior knowledge and overlap may save time; retention and project work may need more. Re-estimate after two completed practice weeks and at later checkpoints.

The table gives emphasis windows within an 18-week model. Topics overlap, and demonstrated readiness can move them earlier or later. Weeks 19–20 are a reserve for weak topics or unfinished project work. The first 14 sessions below remain the concrete starting plan with the expanded time budget. Interview practice begins earlier in small doses; applications can begin when relevant readiness checks pass.

| Approximate weeks | Main emphasis | Evidence we want |
| --- | --- | --- |
| 1–2 | Formal DSA foundations: requirements, Python lists/indices/dictionaries/sets, frequency counting, basic operation counts and Big O, and Arrays & Hashing. Pointer reasoning only if these are secure. Job lifecycle and RAG diagnosis alongside. | Correct small traces, explanations and implementations; identify which prior work is retained and which concepts or Python operations need teaching. |
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

Initially reserve **3–4 hours per week for hands-on labs within the systems/AI allocation**. Once the labs are ready, allocate **six core hours weekly to the showcase project in weeks 9–16**, replacing some new-topic time; reserve about four hours weekly for project polish in weeks 17–18. These hours are inside the 21 core hours, not additions to the 24-hour ceiling or promises to spend catch-up time twice. Keep at least two substantive coding sessions and due reviews in every project-heavy week. Target **one polished project plus two focused labs**. Candidates are an evaluated document assistant, a reliable LLM gateway, or the learner-proposed [Queue and Worker Playground](QUEUE_PLAYGROUND.md), which extends the worker-recovery lab. Select one, then finish it before considering a second showcase project. Keep the AI evaluation lab in every path. See [LABS.md](LABS.md) for acceptance criteria.

Expected outcome is stronger independent problem solving and practical AI/backend engineering evidence. Unseen-medium performance must be demonstrated on multiple mixed tasks; selected hard problems are a stretch goal. A completed calendar, problem count, or predicted `/10` rating is not evidence of top-company readiness. Use the [assessment rules](ASSESSMENT.md) and appropriately scoped mocks to make that decision.

## First two practice weeks: 14 planned sessions

These are relative slots, not dated claims. D07 and D14 are the Sunday slots in a Monday-start template, including 45 minutes of recap within that day's core budget and remaining time for consolidation or lab work. If starting midweek, move the next recap to the actual Sunday and keep the full lessons in order. Saturday and Sunday each have up to 90 additional flex minutes. A missed lesson stays pending.

Choose one main NeetCode problem or foundation exercise per session initially. If time remains after a correct explanation, implementation, and tests, use a changed example or a second appropriately sized problem. Do not force a daily problem quota. Previously completed problems get a cold attempt before teaching. The exit check follows the independent/assisted rules in [ASSESSMENT.md](ASSESSMENT.md).

| Slot | DSA or recap work | Systems/AI focus | Evidence to retain |
|---|---|---|---|
| D01 | Guided Python lists, indices, set/dictionary purpose, simple counting, and input/output reasoning | Job lifecycle and one failure trace | Guided notes and exit evidence; new assessment scores remain null |
| D02 | What work an algorithm performs: trace one loop and nested loops, introduce basic time/space notation, then a tiny duplicate check | Separate retrieval quality from answer quality in a document assistant | Manual operation counts and a explained, small implementation |
| D03 | Sets, dictionaries, membership, and duplicate detection; revisit Contains Duplicate after the concept lesson | State what a worker must claim atomically, with a concrete example | Explain each stored value, operation, and relevant test |
| D04 | Frequency counting and equality of counts; Valid Anagram if the small counting exercise is secure | Define relevant documents, correct answers, and an evaluation baseline | Count trace, correctness explanation, and duplicate cases |
| D05 | Two Sum: derive a correct straightforward approach, then explain what stored information could avoid repeated work | Examine worker crash, retry, and stale ownership | Distinct-index reasoning, tests, and an operation-count comparison |
| D06 | Consolidate Arrays & Hashing using a weak prior problem or a changed small task; teach prerequisites before Group Anagrams or prefix/suffix exercises | Build a tiny held-out evaluation table in the lab | Initial attempt, help level, and the exact concept needing repair |
| D07 | 45-minute recap of the actual completed week; use remaining core time for recall and weak-topic repair | Continue the current lab and adjust workload | Weekly review; pending work remains pending |
| D08 | Repair the weakest foundation or teach the next Arrays & Hashing concept; use one representative prior problem | Distinguish local locking from coordination across replicas | A clear trace and reasoning for each state update |
| D09 | If collection and array reasoning checks pass, introduce Two Pointers with a manual trace and Valid Palindrome; otherwise continue foundations | Calculate and interpret one retrieval metric on tiny examples | Justify pointer movement or explain the repaired foundation |
| D10 | Continue the current topic; use Two Sum II only if sortedness and pointer reasoning are understood | Explain what an idempotency key does and does not guarantee | Reasoning about a changed example, with assistance recorded |
| D11 | Introduce Stack with a tiny push/pop trace and Valid Parentheses only if the current topic is ready to advance; otherwise repair it | Trace one AI failure from input through retrieval to answer | Explain the structure's purpose, operations, and a useful test |
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

Follow [REPORTING.md](REPORTING.md) for the report format, measures and resulting coaching decisions. Give brief feedback after every actual session, use the existing weekly recap for the weekly report, and combine it with the fortnightly checkpoint when both fall in the same period. Broader mock reviews can recur at four-week intervals when coverage supports them. Reports and checks replace existing logging, recap or practice blocks rather than adding hours. With no new evidence, preserve the previous assessment and report that limitation.

- Reviews use gaps of **1, 3, 7, 14, then 30 days after the previous successful learning/review event**. These are growing gaps, not offsets from the first attempt. After the final step, continue 30-day maintenance when useful.
- Initial teaching may create a next-day review; it is not an independent pass. An incorrect or hinted review resets the item to a next-day review. Advance the interval only on an independent success on or after its due date. Early retries preserve the original due date and stage.
- Use the actual completion timestamp when recording a review. A late review advances from its real successful date; missed dates do not create fictional attempts.
- Every 7 days after the first completed session, review completed work, backlog, and time spent. No completed work means a scheduling check, not a learning score.
- At 14 days, review cumulative evidence from the actual lessons. If coverage is too thin, record that and continue the unfinished block.
- After 28 days, run a balanced mock only if there is enough independent coding, systems, and AI evidence to make it useful. Otherwise use the session to repair the weakest foundation and record why the mock was deferred.

The [tracker](../tools/tracker.py) records actual attempts and due reviews. [README](../README.md) explains the repository workflow. Scores describe demonstrated work at a point in time; they are not a fixed estimate of ability.
