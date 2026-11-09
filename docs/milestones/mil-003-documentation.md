# Milestone 003 - Documentation

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-003 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | [9d708b8] |

---

## Purpose

Decide whether the repository explains itself to S02 and S03: README with screenshots, a three-language wiki that records what each lecture step taught, and a repository description with topics.

## Deliverable

README with a screenshot per lecture step, a wiki in `docs/wiki/` in English, Danish and Bahasa Malaysia with the same page set, the screenshots as files in the repository, and the description and topics set on the git host.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | At least one screenshot per lecture step exists as a file and is shown in the README and the wiki | Yes | No |
| 2 | The wiki has the same page set in en, da and ms, and `check-languages.sh` and `check-readme.sh` report no error | Yes | No |
| 3 | Every wiki page states what was gained in the lecture step | Yes | No |
| 4 | The repository description and topics are set on the git host | Yes | No |
| 5 | The wiki review against `QC-WIKI` is a Go | Yes | No |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-002] | The screenshots show the finished application |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 4 | [BC-001] |
| Success criteria 5 and 6 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in) |

## Target Date

2026-11-14 — inside the one-week plan window.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Capture screenshots per lecture step | Run the application in a Docker container with a headless browser and save one screenshot for each lecture step to the repository, so that no GUI is driven on the host desktop (`framework/process/gui-testing.md`). | No | |
| 2 | Extend the README with screenshots | Add the screenshots, the run and test instructions and the template credit to the README so that S02 can follow the steps. | No | |
| 3 | Write the English wiki | Write the wiki pages in English that explain what was gained in each lecture step, with the screenshots. | No | |
| 4 | Translate the wiki to Danish and Bahasa Malaysia | Translate every English page page by page into Danish (`-da`) and Bahasa Malaysia (`-ms`), with the sidebar and language lines. | No | |
| 5 | Set repository description and topics | Set the description and topics on the git host through its API so that S03 finds the repository. | No | |

---

[BC-001]: ../business-case.md
[MIL-002]: ./mil-002-name-card.md
[9d708b8]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/056-name-card/commit/9d708b837307d80c2675f65cdaed97c31d0bd133
