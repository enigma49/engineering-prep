# Starting baseline

This records observations from a short, guided conversation. It was not a standard timed interview, a code review, or a complete assessment. Follow-up prompts helped explore the answers, so prompted progress is not the same as an independent solution. Use this page to choose practice, not to assign a permanent score.

## Observed and reported

| Area | Evidence available | Next useful check |
| --- | --- | --- |
| DSA practice history | The learner clarified the earlier approximate count to exactly 27 previously studied problems, identified from the first 27 entries of the supplied HTML list. Their dates, assistance levels, independent correctness, and present retention remain unknown. | Use [the imported prior-study list](../data/prior_practice.json) to select representative checks after the relevant concepts are introduced. |
| Formal DSA background | This is the learner's first structured DSA study. They report knowing a few concepts without understanding them well. Prior problem exposure does not establish formal foundations. | Teach basic structures, operations, reasoning, and complexity explicitly; use small examples before timed unfamiliar problems. |
| Python familiarity | The learner later reported knowing some Python basics and chose Python for DSA practice. Fluency has not been assessed. | Check functions, loops, lists, dictionaries, and sets within the first guided sessions; separate language help from algorithmic help. |
| DSA reasoning | The sampled problem did not reach a correct independent solution. The discussion exposed a misunderstanding of the concept needed for that problem. One problem cannot establish ability across all patterns. | Explain the relevant invariant, work a small example, then attempt a different problem using that concept without help. |
| Practical systems | Proposed useful components for document processing: batching, content-based caching, fallback processing, queues, retries, dead-letter handling, and logs. | Explain each component's purpose, limits, and failure behavior in a small working lab. |
| Worker recovery | Recognized abandoned work and proposed heartbeat-based recovery. An exact atomic ownership check at result publication was not established. Separate reads and writes leave a possible race. | Demonstrate that a resumed stale worker cannot publish after a replacement takes ownership. |
| RAG diagnosis | Independently distinguished retrieval from generation and proposed plausible failures involving source freshness, ingestion, embeddings, stale chunks, caches, and prompts. | Turn these hypotheses into reproducible checks against a small corpus. |
| AI evaluation | Mentioned datasets, guardrails, and avoiding regressions. Trusted labels, held-out examples, explicit metrics, baseline comparisons, and release criteria were not specified. | Build the small evaluation lab in [LABS.md](LABS.md). |
| Ownership and leadership | The final ownership question was skipped. | Unassessed; revisit separately if useful. |

The proposed attempt-specific record design is not proven impossible. It could prevent stale publication if its actual write operation enforces ownership atomically, cannot recreate a deleted attempt, and handles a failed conditional write correctly. Those implementation details were not established in the conversation.

The supplied prior-study list groups the 27 problems as Arrays & Hashing (9), Two Pointers (5), Stack (7), and Sliding Window (6). Its Stack section includes Generate Parentheses, which our stable catalog places under Backtracking as `nc-072`. The imported IDs are `nc-001` through `nc-026` plus `nc-072`; `nc-027` Binary Search is not included. Preserve the original catalog grouping and record the source grouping separately. HTML checkbox state and estimated durations are not evidence of completion, actual time, or mastery.

Use a foundations-first DSA baseline for instruction. The earlier mock sampled a difficult application before the conceptual background was established; it should not be read as a full interview-readiness score or as a measure of general software-engineering ability. Study history and the learner's reported gaps guide teaching; independent evidence will come from future attempts.

## What this does not establish

There is not enough evidence to rate overall DSA, broad system design, AI expertise, implementation quality, or hiring readiness. Capacity estimation, database and networking depth, model fundamentals, leadership, and independent project ownership remain largely untested. This conversation neither verifies nor disproves prior work experience.

## How to update the baseline

- Keep attempts honest: distinguish independent, hinted, solution-assisted, and revisited work.
- For DSA, record the approach, correctness, time spent, help used, and one specific error or lesson. Familiar-problem recall and unseen-problem transfer are separate checks.
- For systems and AI, link a runnable test or evaluation report before claiming a behavior is demonstrated. Designs and planned work stay labeled as such.
- At Sunday review, note one demonstrated improvement and the next gap. A missed session or failed attempt is information for planning, not a personal rating.

Current priority: build DSA fundamentals consistently while using small systems and AI exercises to make correctness and evaluation concrete.
