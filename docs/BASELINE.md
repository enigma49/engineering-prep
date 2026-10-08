# Starting baseline

This records observations from a short, guided conversation. It was not a standard timed interview, a code review, or a complete assessment. Follow-up prompts helped explore the answers, so prompted progress is not the same as an independent solution. Use this page to choose practice, not to assign a permanent score.

## Observed and reported

| Area | Evidence available | Next useful check |
| --- | --- | --- |
| DSA practice history | About 30 NeetCode problems were reportedly studied. Their titles, outcomes, and independent completion status were not established. This is self-reported exposure, not 30 verified solves. | Record known titles when available; establish a fresh baseline through tracked attempts. |
| Python familiarity | The learner later reported knowing some Python basics and chose Python for DSA practice. Fluency has not been assessed. | Check functions, loops, lists, dictionaries, and sets within the first guided sessions; separate language help from algorithmic help. |
| DSA reasoning | The sampled problem did not reach a correct independent solution. The discussion exposed a misunderstanding of the concept needed for that problem. One problem cannot establish ability across all patterns. | Explain the relevant invariant, work a small example, then attempt a different problem using that concept without help. |
| Practical systems | Proposed useful components for document processing: batching, content-based caching, fallback processing, queues, retries, dead-letter handling, and logs. | Explain each component's purpose, limits, and failure behavior in a small working lab. |
| Worker recovery | Recognized abandoned work and proposed heartbeat-based recovery. An exact atomic ownership check at result publication was not established. Separate reads and writes leave a possible race. | Demonstrate that a resumed stale worker cannot publish after a replacement takes ownership. |
| RAG diagnosis | Independently distinguished retrieval from generation and proposed plausible failures involving source freshness, ingestion, embeddings, stale chunks, caches, and prompts. | Turn these hypotheses into reproducible checks against a small corpus. |
| AI evaluation | Mentioned datasets, guardrails, and avoiding regressions. Trusted labels, held-out examples, explicit metrics, baseline comparisons, and release criteria were not specified. | Build the small evaluation lab in [LABS.md](LABS.md). |
| Ownership and leadership | The final ownership question was skipped. | Unassessed; revisit separately if useful. |

The proposed attempt-specific record design is not proven impossible. It could prevent stale publication if its actual write operation enforces ownership atomically, cannot recreate a deleted attempt, and handles a failed conditional write correctly. Those implementation details were not established in the conversation.

## What this does not establish

There is not enough evidence to rate overall DSA, broad system design, AI expertise, implementation quality, or hiring readiness. Capacity estimation, database and networking depth, model fundamentals, leadership, and independent project ownership remain largely untested. This conversation neither verifies nor disproves prior work experience.

## How to update the baseline

- Keep attempts honest: distinguish independent, hinted, solution-assisted, and revisited work.
- For DSA, record the approach, correctness, time spent, help used, and one specific error or lesson. Familiar-problem recall and unseen-problem transfer are separate checks.
- For systems and AI, link a runnable test or evaluation report before claiming a behavior is demonstrated. Designs and planned work stay labeled as such.
- At Sunday review, note one demonstrated improvement and the next gap. A missed session or failed attempt is information for planning, not a personal rating.

Current priority: build DSA fundamentals consistently while using small systems and AI exercises to make correctness and evaluation concrete.
