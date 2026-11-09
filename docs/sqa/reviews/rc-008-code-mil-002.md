# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-008 |
| CrossReference | [MIL-002], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | [009bdfa] |

---

## Artifact Under Review

- Instance reviewed: [MIL-002]
- Checklist used: [QC-PY-001]
- Scope: full review of the Python code delivered by MIL-002 (src/name_card, tests)
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | PEP 8 casing throughout (Profile, SocialLink, GetCardUseCase, home). |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose; no abbreviations beyond common ones. |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | ruff check and ruff format --check pass with no suppressions. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | All functions are annotated, including -> None. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No exception handling; none swallowed. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults; the repository default is None. |
| 7 | Files, locks and connections are managed with context managers | Pass | No files are opened by the code. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Doxygen docstrings on all public modules, classes and functions. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No logging or print; no personal data beyond the card content S01 supplied. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | no Design Class Diagram exists for this technical project; classes follow the layers in the clean-architecture skill and the deviation is recorded in the traceability matrix notes. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 22 pytest tests (unit and integration) named for behaviour; no network, no order dependence. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | mypy --strict reports no issues in 12 source files; no Any is used. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | Flask is declared in pyproject.toml and used; pytest is a test extra. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | Each constant is defined once in constants.py; the template reads the profile instead of repeating text. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | domain imports nothing; application imports domain; infrastructure imports application and domain; presentation imports infrastructure only in the composition root (app.py), with a comment. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | Single-responsibility modules; the repository is a narrow Protocol and the use case depends on it, not on the concrete class. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | domain, application, infrastructure and presentation packages under src/name_card; unit and integration tests under tests/ (e2e folder kept empty until screenshots in MIL-003). |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | File and folder names are English, lowercase with underscores. |

## Overall Verdict

Go — All mandatory criteria pass; ruff check, ruff format and mypy --strict are clean and 22 tests pass. The host OpenGrep scan flagged `home` as an unused inner function (false positive); it was fixed by returning the view from a module-level `make_home`, without suppression.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | 2026-11-09 |

---

[MIL-002]: ../../milestones/mil-002-name-card.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
[009bdfa]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/056-name-card/commit/009bdfae68150039d08cca7442a7a76bcf3e03f6
