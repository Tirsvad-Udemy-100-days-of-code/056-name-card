# Stakeholder Analysis

## Metadata
| Key | Value |
| --- | --- |
| ID | SA-001 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | [9d708b8] |

---

## Purpose

This analysis identifies who influences or uses the 056-name-card project, so that later documents can cite stable stakeholder IDs. It uses a Power/Interest grid and the FURPS+ model.

## Stakeholder Summary Table

| ID | Name | Role/Title | Organization | Power Level | Interest Level | Quadrant | Primary Concern (Business Language) |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S01 | Jens Tirsvad Nielsen | Course participant, Product Owner, developer and reviewer | UCL Odense (datamatiker student) | HIGH | HIGH | Manage Closely | A finished, personalised name card that completes the assignment |
| S02 | Udemy course participants | Readers and users of the code | Udemy | LOW | HIGH | Keep Informed | Readable, runnable code with the assignment's function names and clear run instructions |
| S03 | GitHub viewers | Repository visitors | Public | LOW | LOW | Monitor | A clear description, topics and README, and no runtime dependencies beyond need |

## Power/Interest Classification Rationale

- **Manage Closely (S01):** decides scope, builds and reviews everything.
- **Keep Informed (S02):** cannot change the project but depends on its README and code quality.
- **Monitor (S03):** browses occasionally; served by a good description and README.

## Primary Concerns and FURPS+ Mapping

| Concern ID | Stakeholder | Concern | FURPS+ attribute |
| --- | --- | --- | --- |
| CN-001 | S01 | The card renders at `/` and looks personal | Functionality |
| CN-002 | S01 | The work is documented and reviewable | Supportability |
| CN-003 | S02 | The code can be installed and run from the README | Usability |
| CN-004 | S02 | The code uses the assignment's names and is easy to read | Supportability |
| CN-005 | S03 | The repository explains itself (description, topics, README) | Usability |
| CN-006 | S03 | No unnecessary runtime dependencies | Implementation constraint |

## Communication Requirements

| ID | Channel | Frequency | Deliverable | Phase / Milestone |
| --- | --- | --- | --- | --- |
| CR-001 | Chat and pull requests | Per milestone | Pull request with closed issues | All milestones |
| CR-002 | README and wiki | Once, updated per milestone | Run instructions, screenshots, lecture notes | Documentation milestone |

## Conflicting Interests and Mitigations

| Conflict | Stakeholders | Mitigation |
| --- | --- | --- |
| S01 keeps personal photo and data in the repository, while S03 sees a public repository | S01, S03 | S01 chose this explicitly; the data is limited to what S01 provided |
| S02 wants the assignment's exact names, while clean structure asks for layers | S01, S02 | Keep the assignment's names in the public functions and keep the layers small |

## Traceability Analysis

### Business Goal Alignment

| Stakeholder | Concern | Business Case objective |
| --- | --- | --- |
| S01 | CN-001 | [BC-001] Objective 1 and 2 |
| S01 | CN-002 | [BC-001] Objective 3 and 4 |
| S02 | CN-003 | [BC-001] Objective 3 |
| S02 | CN-004 | [BC-001] Objective 3 |
| S03 | CN-005 | [BC-001] Objective 4 |
| S03 | CN-006 | [BC-001] Objective 3 |

## Sign-Off

Prepared by the author; reviewed by S01 (AI as stand-in, autonomous mode).

---

[BC-001]: ./business-case.md
[9d708b8]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/056-name-card/commit/9d708b837307d80c2675f65cdaed97c31d0bd133
