# Engineering Prep

A daily learning workspace for data structures and algorithms, system design, and applied AI. The aim is to build correct independent solutions, retain concepts, and produce working projects with evidence.

**Current stage:** foundations. **Next session:** [Day 1](docs/DAY_01.md). **Daily schedule:** awaiting the learner's availability; no reminder is active.

**Practice language:** JavaScript. Use Node.js for local exercises and project code. The assistant can operate the existing Python tracker; learning Python is not part of this preparation plan.

## Start a session

Open this repository in your coding assistant and say:

> Start today's practice. Read AGENTS.md and the progress files, check due reviews, and guide me through one question at a time. Teach first where needed; keep independent checks separate. Save an evidence-based assessment and the next review dates when we finish.

The initial workload is **90 minutes on six days per week**, plus a **20-minute weekly recap**. These are provisional budgets, not obligations. A 30-minute fallback keeps reviews moving on busy days. We will adjust the workload after the first week and after reviewing the learner's actual schedule.

Allow a provisional **36–44 weeks** for broad preparation and one finished showcase project at this workload. This is a planning estimate, not a completion or hiring promise. See the [timeline and topic scope](docs/PLAN.md#provisional-timeline-and-topic-scope); revise it after the first two practice weeks.

## What to open

| File | Purpose |
| --- | --- |
| [Plan](docs/PLAN.md) | First two weeks, later stages, and advancement criteria |
| [Day 1](docs/DAY_01.md) | The first guided session; not yet completed |
| [Baseline](docs/BASELINE.md) | Specific observations from the initial diagnostic |
| [Assessment](docs/ASSESSMENT.md) | Transparent daily ratings and how help is recorded |
| [Progress](PROGRESS.md) | Dashboard generated from recorded practice |
| [Tracker](docs/TRACKER.md) | Local commands and review scheduling |
| [Systems and AI labs](docs/LABS.md) | Small experiments that lead toward portfolio projects |
| [Sources](docs/SOURCES.md) | Curriculum references and provenance |

## How progress works

- NeetCode 150 is the DSA problem bank. The overlapping problems in the earlier prep plan become retention checks and unfamiliar variations.
- Roughly 30 problems were previously studied, but their identities and assistance levels have not yet been imported. The tracker does not pretend they were never studied or mark unknown items independently solved.
- After practice, record whether the work was learned, independent, hinted, or needs review, with a short evidence note.
- Review gaps grow through **1, 3, 7, 14, and 30 days after the previous successful scheduled review**. A hint or failed recall brings the item back the next day. Early retries are logged but preserve the existing due date and stage; only an independent attempt on or after that date advances the interval.
- Missing a day leaves reviews due. It does not create a failing score or silently advance the curriculum.
- Daily ratings describe the assessed task and assistance. Untested dimensions remain unassessed. There is no permanent global ability score.

```sh
python3 tools/tracker.py today
python3 tools/tracker.py dashboard
python3 -m unittest discover -s tests -v
```

Record real practice only; see [tracker instructions](docs/TRACKER.md) for examples. The assistant can maintain these files during sessions, so using the commands manually is optional.

## Repository layout

```text
docs/             curriculum, baseline, rubric, and session guides
data/             problem catalog, concept catalog, and review history
sessions/         dated session notes and assessments
practice/dsa/     learner-written solutions and explanations
practice/systems/ diagrams, failure timelines, and experiments
practice/ai/      evaluation cases, measurements, and experiments
projects/         later portfolio implementations
tools/            dependency-free progress tracker
tests/            tests of the tracker, not a substitute for learning checks
```

This is a public learning repository. Use public or synthetic data. Keep private documents, employer material, credentials, and raw personal conversations outside tracked files. The existing resume and preparation PDF are not uploaded.
