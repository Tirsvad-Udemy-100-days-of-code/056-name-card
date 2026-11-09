# Milestone 001 - Scaffold

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | pending |

---

## Purpose

Decide whether the project skeleton is ready to receive the application: configuration, tooling, documentation of the local environment and a passing smoke test.

## Deliverable

A Python project with `pyproject.toml` (Python 3.13 or newer, Flask as the only runtime dependency, pytest as a test extra), `constants.py`, a Python `.gitignore`, a Doxyfile, a README with `.venv` and test instructions, and one passing pytest test.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `pyproject.toml` declares `requires-python = ">=3.13"` and exactly one runtime dependency | Yes | No |
| 2 | A fresh `.venv` installs with the README commands and `python -m pytest` exits 0 | Yes | No |
| 3 | `constants.py` exists and holds the constants used by the code | Yes | No |
| 4 | `doxygen Doxyfile` runs without errors | Yes | No |
| 5 | `.gitignore` ignores `.venv`, `.env` and `docs/ai-prompts/` | Yes | No |
| 6 | The Python code review against `qc-programming-python` is a Go | Yes | No |

## Dependencies

| Depends on | Reason |
| --- | --- |
| None | First gateway |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 3: tests, README, Doxygen and `.venv` guide | [BC-001] |
| Success criteria 3 and 4 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in) |

## Target Date

2026-11-10 — inside the one-week plan window; the Business Case sets no fixed duration.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Add pyproject.toml and package layout | Create `pyproject.toml` with Python 3.13 or newer, Flask as the only runtime dependency and pytest as a test extra, and the `src/` and `tests/` layout, so that S02 can install the project with one command. | No | |
| 2 | Add constants.py | Hold the application constants (template name, folders, host and port) in one module so that no literal is repeated in the code, as the course requirements ask. | No | |
| 3 | Add .gitignore and Doxyfile | Add the Python `.gitignore` (with `.venv`, `.env`, `docs/ai-prompts/` because the repository is public) and a Doxyfile that documents `src/` from the Doxygen comments. | No | |
| 4 | Add README with environment guide | Write the README from the framework template with how to create and use a local `.venv`, upgrade pip, run the application and run the tests, for S02 and S03. | No | |
| 5 | Add smoke test | Add a pytest test that proves the package imports and the constants are defined, so the test setup is proven before the application exists. | No | |

---

[BC-001]: ../business-case.md
