# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-011 |
| CrossReference | [MIL-004], [QC-PY-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Proposed | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [MIL-004]
- Checklist used: [QC-PY-001]
- Scope: Python code delivered by MIL-004 (tools/background/generate.py, tests) and the stylesheet and template change
- Language and domain: n/a (technical type)
- Language reviewer: none
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Packages, modules, functions, variables, classes and constants follow PEP 8 casing (`snake_case`, `PascalCase`, `UPPER_SNAKE`) | Pass | PEP 8 casing: build_svg, code_block, binary_rows, network; constants in upper case. |
| 2 | Names state purpose in the domain's language; no unexplained abbreviations, no single-letter names outside tiny scopes | Pass | Names state purpose (binary_rows, code_block, network). |
| 3 | Code is produced by the project's formatter and passes its linter with no unexplained suppressions | Pass | ruff check and ruff format --check pass on src, tests and tools with no suppressions; an unused noqa in tools/screenshots/capture.py was removed. |
| 4 | Every function and method signature is type-annotated, including `-> None` | Pass | All functions are annotated, including -> None and -> int. |
| 5 | No bare `except:`, no swallowed exceptions; specific exceptions are raised and the cause is kept (`raise ... from`) | Pass | No exception handling; none swallowed. |
| 6 | No mutable default arguments and no shadowed builtins | Pass | No mutable defaults; the random generator is created per call from a fixed seed. |
| 7 | Files, locks and connections are managed with context managers | Pass | The only file written is the SVG, with Path.write_text and encoding utf-8. |
| 8 | Public modules, classes and functions have docstrings that say what, not how | Pass | Doxygen file header and docstrings on the module and every function; constants have ## comments. |
| 9 | Logging uses `logging`, not `print`; no secrets or personal data in log output | Pass | No logging; the generator prints the output path only; no personal data is added. |
| 10 | Classes and operations trace to the Design Class Diagram they implement; deviations are recorded | N-A | no Design Class Diagram exists for this technical project; the generator is a script outside src. |
| 11 | Tests exist for new behaviour, are named for the behaviour, and do not depend on order or the network | Pass | 7 new tests: well-formed and repeatable SVG, motifs present, the committed bg.svg equals the generator output, stylesheet order, portrait rule and the served background. 29 pass; no network and no order dependence. |
| 12 | Type checker runs in strict mode without errors; `Any` is justified in a comment | Pass | mypy --strict reports no issues in 17 source files; no Any is used. |
| 13 | Dependencies are declared and pinned in the project's dependency file, none unused | Pass | No new dependency; the generator uses only the standard library and Flask stays the only runtime dependency. |
| 14 | Each piece of knowledge (a business rule, constant, format, validation or query) is defined in one place; code is merged only where it expresses the same knowledge, not where it merely looks alike | Pass | The portrait size and the background path are each defined once, in card.css; the code samples are one constant. |
| 15 | Imports point inward: business-rule modules import no framework, database, UI or delivery-mechanism code, and there are no import cycles | Pass | The generator is outside src and imports nothing from the application; the layers of src are unchanged. |
| 16 | SOLID holds: a class or module has one reason to change; new behaviour is added by extension, not by editing a type test in several places; subclasses honour the contract of their base; protocols are narrow; high-level code depends on protocols or abstract types and receives its implementations | Pass | Each function has one job: code lines, binary rows, network, document. |
| 17 | Source is laid out in the layers and folders of the clean architecture folder structure (`domain`, `application`, `infrastructure`, `presentation` packages under `src/`, and `unit`, `integration` and `e2e` under `tests/`), in `snake_case`, and imports between the layers point inward | Pass | tools/background next to tools/screenshots; tests in tests/unit and tests/integration. |
| 18 | File and folder names are English, contain no space and no character outside letters, digits, `-`, `_` and `.`, and follow the casing of the language for files | Pass | File and folder names are English, lowercase with underscores. |

## Overall Verdict

Go — All mandatory criteria pass; ruff check, ruff format and mypy --strict are clean, 29 tests pass, and the step 4 screenshot shows the portrait centred on the new background.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | 2026-11-09 |

---

[MIL-004]: ../../milestones/mil-004-portrait-and-background.md
[QC-PY-001]: ../../../framework/qc/code/qc-programming-python.md
