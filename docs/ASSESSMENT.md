# Assessment and evidence rules

Assess what was demonstrated on a specific task. Do not infer general ability, hiring readiness, or knowledge of untested topics from one answer. See [baseline](BASELINE.md), [practice plan](PLAN.md), and [Day 1](DAY_01.md).

## Baseline and public record

The starting evidence identifies gaps in interpreting a time-window invariant, reasoning about atomic job ownership, and defining AI evaluation metrics. These are practice targets, not permanent labels or a complete skill inventory.

The earlier brief diagnostic was assisted in places and did not test the full curriculum. Resume experience is useful context for choosing examples; it is not a substitute for demonstrated answers. The tracker begins with actual recorded practice, not fabricated historic sessions.

The learner has clarified that this is their first formal DSA study and identified 27 previously studied problems. Treat concept knowledge as unestablished until checked; do not use an unfamiliar timed problem as the first introduction to an untaught structure or algorithm. Use a brief, ungraded concept check to choose teaching depth, then assess appropriately scoped independent application after instruction. Neither the prior-study record nor a teaching conversation creates a completed review or a numeric score.

Public notes contain task summaries, code or lab evidence, help used, and a short reflection. Exclude personal information, employer details, proprietary examples, and raw interview transcripts.

## Separate teaching from assessment

1. State whether the activity is new-topic learning or assessment of covered material. Teach unfamiliar prerequisites with an explanation and worked example first; start an independent attempt only when the task is appropriate for the learner's current preparation. A brief familiarity check must not become a chain of diagnostic follow-ups before teaching.
2. Record the attempt before explaining the solution. A neutral request to test or clarify is not the same as giving a strategy.
3. Teach and practice openly; help is expected during learning.
4. Label any immediate reproduction of the taught approach as guided practice.
5. Test retention later without notes. Use a materially changed example or task to examine transfer; familiar syntax alone does not demonstrate derivation.

Do not overwrite a failed initial attempt with a successful guided answer. If a solution was supplied, implementation may still provide evidence, but independent derivation was not demonstrated.

## Daily topic rubric: 0–4

Use the four dimensions below for the topic actually assessed. A brief session may assess only one or two dimensions. Store the others as `null`, not zero.

| Score | Common anchor |
|---|---|
| 0 | The assessed requirement was not demonstrated; the answer is absent or fundamentally incorrect |
| 1 | Some relevant understanding is visible, but major gaps prevent a correct application |
| 2 | A basic case works; important boundaries, reasoning, or validation remain incomplete |
| 3 | Independently gives a substantially correct answer, explains it, and handles ordinary follow-ups |
| 4 | Independently justifies correctness, handles meaningful edge cases, and adapts to a changed requirement |

Assistance is recorded separately. A guided artifact can be correct without earning an independent 3 or 4. Leave an unassessed independent dimension `null`; retain any earlier independent score rather than replacing it with the coached result.

### DSA anchors

| Dimension | 0–1 evidence | 2 evidence | 3–4 evidence |
|---|---|---|---|
| Specification and model | Misreads the contract or cannot define a valid candidate | Basic examples are right; some boundaries are unresolved | Correct contract, invariant, and edge cases; adapts to changed bounds |
| Derivation and correctness | No correct approach or an unjustified pattern guess | Correct straightforward approach or partly justified optimization | Derives a correct approach and explains why it works; distinguishes alternatives |
| Implementation | Code fails core behavior | Main path works with repairable omissions | Code implements the approach correctly, including relevant state updates and boundaries |
| Validation and complexity | Accepts a wrong trace or cannot justify costs | Tests normal cases; cost explanation is partial | Uses counterexamples and edge cases; correctly derives time and space costs |

For a timestamp-window task, assess membership over the entire window, duplicate-user state, expiry, and the return contract. Do not mistake consecutive small gaps for proof that every retained event fits one window. Complexity remains `null` if it was not discussed.

### Systems and concurrency anchors

| Dimension | 0–1 evidence | 2 evidence | 3–4 evidence |
|---|---|---|---|
| Requirements and model | Names components without a coherent goal | Basic workload and flow are plausible | Defines useful requirements, state, boundaries, and measurable constraints |
| Correctness and ownership | Does not identify the race or assumes ownership | Sees the race but leaves enforcement incomplete | States the invariant and explains how ownership is enforced under concurrency |
| Failure and recovery | Ignores retries, crashes, or stale actors | Handles one failure with unresolved consequences | Traces important failures and recovery; qualifies guarantees and external effects |
| Tradeoffs and validation | Selects tools without reasons | Gives one relevant tradeoff or test | Compares options against requirements and proposes useful validation |

A process-local mechanism does not automatically establish coordination across replicas. Ask the learner to explain the mechanism they chose; do not award points merely for naming locks, leases, queues, or transactions.

### Applied AI and evaluation anchors

| Dimension | 0–1 evidence | 2 evidence | 3–4 evidence |
|---|---|---|---|
| Pipeline and diagnosis | Gives generic fixes without locating the failure | Identifies a plausible stage and one check | Separates failure sources and uses observable evidence to isolate them |
| Evaluation design | No useful test set, labels, or comparison | Small test set and baseline with limitations | Representative held-out cases, explicit labels, and a repeatable comparison |
| Metrics and interpretation | Metric name without a correct meaning | Computes a simple metric but misses limitations | Defines and interprets relevant retrieval/answer metrics and their limitations |
| Production reasoning | Ignores practical consequences | Identifies a relevant constraint | Explains cost, latency, reliability, or access tradeoffs supported by evidence |

An applied-LLM score does not assess ML mathematics, model training, fine-tuning, or deep inference infrastructure. Those topics remain untested until specifically assessed.

## Help, timing, and task context

Record the task/topic, prior exposure, actual active minutes, artifact or summary, assessed dimensions, and help:

- **Independent:** no strategy or correction supplied.
- **Neutral prompt:** asks for clarification, a trace, or testing without directing the solution.
- **Directional hint:** reveals a relevant strategy, missing condition, or likely failure.
- **Solution supplied:** provides the main approach, code, or decisive correction.

Record the highest help level and what it affected. A hint about an API may affect implementation without supplying the algorithm. A hint supplying the invariant affects derivation. The record should make that distinction visible.

Use the real timebox from [PLAN.md](PLAN.md). Log unfinished work honestly. Pauses and tool setup are not problem-solving time. Do not change the rating simply because the learner typed slowly; report elapsed time separately.

Use JavaScript for current DSA practice and distinguish language/API difficulty from algorithmic difficulty. A syntax reference or help using an already-chosen operation can affect implementation independence without supplying the algorithm. A suggestion to introduce a `Map`, heap, or memoization may reveal the approach and must be classified accordingly. Record what was looked up, which dimension it affected, and actual time; do not silently exclude lookup time or convert an assisted implementation into an independent solve. Teach JavaScript details inside the existing learning budget as needed. Tutor-run tests verify the artifact; they do not establish that the learner independently designed or explained those tests. Day 1 remains ungraded.

For each timed problem, retain the task/source, prior exposure, whether its category was revealed, practice mode, agreed timebox, actual timing when measured, deadline snapshot, and any later assisted work. Ordinary learning attempts can begin after clarification. Speed benchmarks and formal mocks count from first presenting the problem, including reading, clarifications, implementation, testing, and explanation; exclude only explicitly recorded non-task interruptions. Compare like timing modes rather than treating all elapsed times as equivalent.

The 20–30-minute unseen-medium target in PLAN.md concerns correct independent completion, not merely recognizing a pattern or recalling familiar code. Record incomplete attempts and the number and scope of problems sampled. Repeated mixed performance, retained knowledge, and help required matter alongside speed. A topic-labeled exercise may demonstrate implementation and reasoning without establishing independent pattern selection.

## Optional numeric summary

For a **single topic and attempt only**, an optional `/10` display is:

`2.5 × mean(non-null assessed dimension scores)`

Always show the topic, number of assessed dimensions, help level, and whether the attempt was independent or guided. With no assessed dimensions, the result is `null`. Do not average DSA, systems, AI, and ownership into an overall ability score. Do not compare different task difficulties as if they were the same test.

Example: a DSA attempt with scores `[2, 1, null, null]` has an optional score of `3.75/10`, based on only 2 of 4 dimensions. It says nothing about implementation or complexity. This is an illustration, not a recorded baseline result.

## Reviews and readiness

Use [REPORTING.md](REPORTING.md) to turn assessments into session feedback, weekly reports, and fortnightly coaching decisions. Compare similar tasks and state the sample size, coverage, help and timing. Report independent application, delayed recall, unfamiliar transfer and project evidence separately. Missing participation logs are unknown, and private timetable details never belong in reports.

- Review gaps are 1, 3, 7, 14, then 30 days **after the previous successful event**, using real completion dates. Hinted or unsuccessful reviews reset to the next day. The final interval may repeat for maintenance.
- An initial teaching session can schedule next-day retrieval, but does not count as independent recall. A successful review must match the item's objective without solution help. Only success on or after the due date advances the interval; early retries keep that due date and stage.
- Weekly reviews summarize evidence and workload; 14-day checkpoints examine retention and transfer across completed topics.
- Consider a mock after 28 days only when the covered material supports a useful independent attempt. Otherwise continue targeted practice and record the reason.
- One strong attempt is encouraging evidence, not mastery. Readiness requires repeated independent work, delayed retention, unfamiliar variants, and appropriately scoped mocks.

Use [tools/tracker.py](../tools/tracker.py) to record practice and review state. The rubric supports learning decisions; it does not promise a company outcome or freeze a learner's future potential.
