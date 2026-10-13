# Small labs and a later portfolio

These are build prompts, not completed projects or reference solutions. DSA remains the first-phase priority. The weekly plan has three core hours daily (21 hours), plus up to 90 flexible minutes on each weekend day (3 hours), for at most 24 hours. Weekend catch-up replaces optional work in those flexible blocks; the same time cannot be counted twice. The 45-minute weekly recap is included in Sunday's three core hours.

A normal 180-minute session allocates 15 minutes to retrieval, 90 to DSA, 45 to systems/AI, 20 to an independent check, and 10 to logging. Initially, reserve **3–4 hours per week within the systems/AI allocation** for hands-on lab work; these hours are not added to it. Split work into short steps and carry unfinished work forward. Use the 30-minute busy-day version when necessary and record what remains pending.

Work on one lab at a time. Start with the worker-recovery lab, then evaluation. A step may span several sessions. Use synthetic or openly licensed public data; keep employer code, customer information, credentials, and private logs out of the repository.

## Lab 1: Can a stale worker publish a result?

**Purpose:** distinguish detecting a missing heartbeat from enforcing who may publish a result.

Build a tiny local job processor with a persistent store and two controllable workers. A synthetic job can transform a short string; no OCR service or model API is needed. Keep the implementation small enough to inspect its reads and writes.

### Steps

1. Write the job states and the correctness rule in plain English. Include what happens when an original worker resumes after a replacement starts.
2. Build the normal path: submit a job, process it, save a result, and retrieve that result.
3. Add worker failure and recovery. Make pauses and restarts controllable in the test setup.
4. Write the failure tests below. Include the sequence where the original worker checks its state, pauses, and resumes after takeover.
5. Inspect the exact publication operation and fix any failed guarantee. Document what happens when the operation does not succeed.
6. Add a short README section with a state diagram, test commands, observed behavior, and remaining limits.

### Required tests and acceptance criteria

| Test | Passing behavior |
| --- | --- |
| Normal completion | The submitted job has a retrievable completed result. |
| Worker dies before completion | A replacement can eventually complete the same logical job. |
| Stale worker resumes after takeover | Its result cannot become the authoritative completed result. |
| Original worker pauses between checking state and publishing | Replacement ownership remains protected when the original worker resumes. |
| Two workers attempt takeover | The store establishes a single current owner for publication. |
| A message or completion is repeated | The logical job does not gain conflicting completed results. |

Use synchronization points or a controllable clock to reproduce interleavings; passing once because of lucky timing is insufficient. Record the exact store operation that enforces the publication rule. Tests must exercise the real implementation, not a mock that assumes ownership enforcement works.

**Done when:** all listed cases pass reproducibly and you can explain why a stale worker's write fails. Also state the limits: protecting result publication does not automatically prevent duplicate model calls or other external side effects.

## Lab 2: Did a RAG change actually improve answers?

**Purpose:** turn plausible debugging hypotheses into a repeatable comparison.

Use a small synthetic document collection containing explicit facts, one updated fact, and questions the documents cannot answer. Begin with a small manually checked set, such as 12 questions. Reserve some questions for development and some untouched for the final comparison. This is a learning-sized test set, not strong statistical evidence of production quality.

### Steps

1. Write reference answers yourself. For each question, label whether it is answerable and identify the supporting document and evidence passage. Use stable document/evidence references so chunking changes do not invalidate the labels.
2. Define baseline configuration A and candidate B. Change one thing initially, such as chunk size. Record corpus version, prompt, retrieval settings, model identifier if used, and run date.
3. Run both configurations against the same questions. Save retrieved evidence, generated answers, latency, and token/cost information when available.
4. Score retrieval and answer quality separately using the table below. Inspect failures instead of relying on one aggregate score.
5. Compare results on the held-out questions only after development. Write a brief decision using acceptance criteria chosen before viewing that comparison.
6. Add regression tests and one command that reproduces the comparison from the saved inputs and configurations.

### Minimum report

| Measure | What to record |
| --- | --- |
| Retrieval evidence hit at k | Among answerable questions, how often the top-k results include the labeled supporting evidence; state k and the denominator. |
| Answer correctness | A manual pass/fail judgment against the reference answer, with a written rule for partial or ambiguous answers. |
| Grounding | Whether the answer's factual claims are supported by the retrieved evidence; inspect cited sources rather than merely checking that citations exist. |
| Unanswerable questions | Whether the system abstains appropriately instead of inventing an answer. |
| Freshness | Whether questions about the updated fact use the current source and answer. |
| Efficiency | Measured latency and, if real model calls are made, token usage and estimated cost. State the workload and how cost was calculated. |

Human-checked references are the starting point. If adding an LLM judge later, compare its judgments with human labels before trusting its score.

### Required tests and acceptance criteria

- A hand-checkable fixture verifies metric calculations, including missing evidence and unanswerable cases.
- Every labeled evidence reference resolves to the intended corpus version.
- Development and held-out question IDs do not overlap.
- An updated-document case detects a deliberately stale answer or stale retrieval result.
- The report includes both configurations, per-question outcomes, regressions, and the decision rule. Do not hide worse cases behind the average.

**Done when:** another person can reproduce the report and understand why candidate B is accepted or rejected. Define a simple release rule before the comparison, such as no regression on designated freshness cases, no unsupported answer on designated unanswerable cases, and quality/cost limits suitable for this toy application. Passing these few cases establishes only their tested behavior.

Saved synthetic model outputs can make an initial offline harness cheap and deterministic. Label them clearly; they demonstrate the harness, not a real model's quality or speed. Later, run real outputs through the same harness. After a one-factor comparison works, compare chunking-only, model-only, and combined changes.

## Later: turn selected work into one showcase project

Begin this stage when the study routine is sustainable and the labs' acceptance criteria are met. In the 18-week planning model, reserve **6 hours per week in weeks 9–16** for one showcase project, then use project blocks in weeks 17–18 for measurements, documentation, and polish. The overall forecast is 16–20 weeks; these windows can move when the evidence warrants it. Project hours come from the existing weekly budget, replacing some new-topic systems/AI work and other planned focus blocks rather than adding another shift. Preserve due reviews and at least two substantive DSA sessions per week. Finish one showcase project before considering another.

The learner has also proposed a [Queue and Worker Playground](QUEUE_PLAYGROUND.md): extend Lab 1 with UI controls, a separate Autocannon load runner, real queue/worker telemetry and reproducible overload/scaling/failure experiments. This is an additional candidate for the same single showcase slot, not an extra mandatory build. It remains proposed and unimplemented. Keep the AI evaluation lab whichever showcase is selected. The brief defines measurements and completion criteria, including the distinction between accepted HTTP requests and completed jobs.

| Stage | Reliable LLM gateway | Evaluated document assistant |
| --- | --- | --- |
| Small working slice | One real provider, a clearly labeled test adapter, typed requests, and observable failure handling. | Ingest public documents, retrieve evidence, and answer with citations. |
| Correctness | Add and test timeouts, cancellation, retries, fallback policy, and relevant job-recovery behavior from Lab 1. | Add update/re-index behavior, abstention, and retrieval/answer regression checks from Lab 2. |
| Measured extension | Add a second real provider, per-tenant limits, and measured load/failure tests. | Compare a simple retrieval baseline with a real hybrid/reranking approach; measure quality, latency, and cost. |
| Public evidence | Publish reproducible benchmark commands, failure scenarios, results, and limits. | Publish the permitted corpus or a download recipe, labeled evaluation set, experiment configurations, results, and limits. |

A showcase project should have a runnable setup, meaningful automated tests, CI, architecture and tradeoff notes, a short demonstration, and reproducible measurements. Clearly mark stubs and unimplemented features. A design document is useful evidence of reasoning; it is not evidence that the system has been built or operated at scale.

For an assistant serving multiple users, add synthetic access-control tests before claiming tenant isolation. For either project, add relevant malicious-input and failure cases before making reliability or security claims.

## Optional AI foundations later

After the core routine is stable, learn basic descriptive statistics, sampling variation, and train/validation/test separation. Use a small public dataset to compare a simple predictive baseline with another model and explain leakage and overfitting. This broadens AI knowledge beyond LLM application engineering.

GPU serving and model training are optional future specializations, not prerequisites for this first phase. Choose them if the target role requires them, with separate hands-on work and time allocated.
