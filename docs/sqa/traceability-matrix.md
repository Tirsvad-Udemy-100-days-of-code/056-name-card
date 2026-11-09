# Traceability Matrix

## Metadata
| Key | Value |
| --- | --- |
| ID | TM-001 |
| CrossReference | [BC-001], [SA-001], [PP-001], [MIL-001], [MIL-002], [MIL-003], [MIL-004] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | [9d708b8] |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Add MIL-004 | pending |

---

## Purpose

Tracks backward/forward links between artifact instances so that the Business Case's
cross-artifact traceability success criterion is measurable. A row is added or
updated whenever an artifact instance is created or reviewed.

## Traceability Table

| Artifact Instance | Type | Language | Domain | Upstream (Backward Link) | Downstream (Forward Link) | Last Reviewed (RC-ID) |
| --- | --- | --- | --- | --- | --- | --- |
| [BC-001] | BC | en | it | - | [SA-001], [PP-001] | RC-001 |
| [SA-001] | SA | en | it | [BC-001] | [PP-001] | RC-002 |
| [PP-001] | PP | en | it | [BC-001], [SA-001] | [MIL-001], [MIL-002], [MIL-003], [MIL-004] | RC-003 |
| [MIL-001] | MIL | en | it | [PP-001] | - | RC-004, RC-007 (code) |
| [MIL-002] | MIL | en | it | [PP-001], [MIL-001] | - | RC-005, RC-008 (code) |
| [MIL-003] | MIL | en | it | [PP-001], [MIL-002] | - | RC-006, RC-009 (wiki) |
| [MIL-004] | MIL | en | it | [PP-001], [MIL-003] | - | RC-010 |

## Concern Coverage

| Concern (CN-ID) | Views that answer it | Decisions (ADR) | Quality check (TP) | Status |
| --- | --- | --- | --- | --- |
| CN-001 | none yet (no views are required for this project) | - | - | Gap |
| CN-002 | none yet | - | - | Gap |
| CN-003 | none yet | - | - | Gap |
| CN-004 | none yet | - | - | Gap |
| CN-005 | none yet | - | - | Gap |
| CN-006 | none yet | - | - | Gap |

## Open Inconsistencies

| # | Views | Inconsistency | Found in (RC-ID) | Status | Resolved in |
| --- | --- | --- | --- | --- | --- |
| - | - | None found | - | Closed | - |

## Coverage Notes

No view artifacts (use cases, domain model, architecture description) exist: the project is a single-page Flask application and all tasks are technical. A concern marked Gap is covered by the milestone tasks and the tests instead; this is recorded here so a later view can close the gap. `-` in Upstream means foundational; in Downstream it means nothing is built on it yet.

---

[BC-001]: ../business-case.md
[SA-001]: ../stakeholder-analysis.md
[PP-001]: ../project-plan.md
[MIL-001]: ../milestones/mil-001-scaffold.md
[MIL-002]: ../milestones/mil-002-name-card.md
[MIL-003]: ../milestones/mil-003-documentation.md
[MIL-004]: ../milestones/mil-004-portrait-and-background.md
[9d708b8]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/056-name-card/commit/9d708b837307d80c2675f65cdaed97c31d0bd133
