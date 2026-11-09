# Business Case

## Metadata
| Key | Value |
| --- | --- |
| ID | BC-001 |
| CrossReference | [SA-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | pending |

---

## Executive Summary

056-name-card is the final project of Day 56 of Udemy's "100 Days of Code: The Complete Python Pro Bootcamp". It serves a web-based name card, built from the html5up "Identity" template, from a small Flask application at the root route. The card shows the name, photo, links and contact information of the course participant (Jens Tirsvad Nielsen). The project is also a public, runnable reference for other course participants. We recommend proceeding: the work is small, has no cost beyond the author's time and has a clear, testable result.

## Methodological and Standards Foundation

The project follows the SQA and QC framework mounted at `framework/` (Business Case, Stakeholder Analysis, Project Plan, milestones, tasks, then code). Every artifact is reviewed against its QC checklist and recorded as an `RC-*`. Quality attributes use ISO/IEC 25010:2023. Source code follows the Python conventions of the `coding-conventions` skill and is reviewed against `qc-programming-python`.

## Problem Statement

The course assignment asks for a personal name card website. The participant needs a finished, personalised result that follows the assignment's folder structure (`templates/`, `static/`) and root route, and that other participants can read, run and compare. Without a documented, tested repository the result is hard to reproduce and gives no learning value to others.

## Business Opportunity

A clear repository shows how a static HTML5 UP template is served by Flask, gives readers screenshots and a per-step explanation in three languages, and serves as a portfolio entry for the author, a datamatiker student at UCL Odense.

## Objectives

1. Serve the html5up "Identity" template at `/` with Flask, using the `templates/` and `static/` folders.
2. Personalise the card: name, photo, background image, text and links, and keep the template's required attribution.
3. Provide automated pytest tests, a README with run and test instructions, Doxygen comments with a Doxyfile, and a `.venv` guide.
4. Provide a wiki in English, Danish and Bahasa Malaysia that explains what each lecture step taught, with a screenshot for each step.

## Scope

### In Scope

- A Flask application with one root route that renders the card.
- The Identity template assets, personalised content and the author's photo.
- `src/`, `tests/`, `docs/`, `pyproject.toml`, `constants.py`, `.gitignore`, Doxyfile and README.
- README and wiki screenshots for each lecture step, and a wiki in en, da and ms.

### Out of Scope

- The sibling project 056-my-personal-site (its own repository and plan).
- Hosting, deployment, a database, a contact form back end and user accounts.
- Further routes or templates beyond the card.

## Expected Benefits

### Tangible Benefits

- A runnable, tested repository reproducing the assignment.
- Documentation (README and a three-language wiki) that readers can follow without help.

### Intangible Benefits

- Practice with Flask templates and static files.
- A presentable portfolio piece for a datamatiker student.

## Strategic Alignment

The project supports the participant's goal of completing the 100 Days of Code course and of practising software architecture, SQA and QC and AI-assisted development, using the same process the participant applies in other work.

## Success Criteria

| # | Criterion | Target | Measure |
| --- | --- | --- | --- |
| 1 | The root route renders the card | `GET /` returns HTTP 200 with the participant's name in the body | pytest test |
| 2 | Static assets resolve | All `static/` links in the page return HTTP 200 | pytest test |
| 3 | Tests pass | 100 % of pytest tests pass on Python 3.13 | `python -m pytest` exit code 0 |
| 4 | Runtime dependencies | Exactly one runtime dependency (Flask) | `pyproject.toml` |
| 5 | Wiki coverage | 3 languages with the same page set | `check-languages.sh` and wiki review |
| 6 | Screenshots | At least one per lecture step in README and wiki | file count in `docs/` |

## Risks

| Risk | Impact | Mitigation |
| --- | --- | --- |
| The template download link has expired | The template cannot be fetched | Use the public html5up demo or stop and ask S01 |
| Personal photo and data are public | Privacy exposure of S01 | S01 asked to keep them; recorded as an accepted choice |
| Template licence (CCA 3.0) is not respected | Licence breach | Keep the attribution footer and credit in the README |
| Screenshots taken on the host desktop | Interrupts S01's work | Take them in a Docker container with a headless browser |
| Translations contain mistakes | Readers are misled | English is authoritative; translations follow page by page |

## Assumptions

- S01 is the Product Owner, developer and reviewer; the AI acts as stand-in reviewer in autonomous mode.
- Docker, Python 3.13 and Doxygen are available on the author's machine.
- The Product Owner's language is English and the domain is IT.

## Constraints

- Python 3.13 or newer, a `.venv`, pytest, `constants.py` and `pyproject.toml`.
- Flask is the only runtime dependency.
- Code lives in `src/` and `tests/`; documents in `docs/`.
- Tokens from `.env` are for personal use and are never imported by the project.

## Cost–Benefit Assessment

| Costs | Benefits |
| --- | --- |
| The author's time (a few hours); no licence or hosting cost. Qualitative assessment is justified because this is a learning project with no revenue. | A reproducible reference, a portfolio entry and documented learning. |

## Stakeholders

| Stakeholder ID (SA) | Interest in this project |
| --- | --- |
| S01 | Owns, builds and reviews the project |
| S02 | Reads and compares the code and the README |
| S03 | Browses the repository for ideas |

## Recommendation

Proceed — the scope is small, the cost is only time and the result is verifiable by tests.

---

[SA-001]: ./stakeholder-analysis.md
