# Milestone 004 - Portrait and background

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-004 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version, change request from S01 | [29d7a1b] |

---

## Purpose

Decide whether the finished name card shows the portrait centred in the card, as the template does, and a background that speaks of software development, AI and machine learning.

## Deliverable

The portrait fits the card and is centred with the horizontal line behind it, a new background image of software development, AI and machine learning, a regenerated step 4 screenshot, and the README and wiki text that describe the background.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | In the step 4 screenshot the portrait is horizontally centred in the card and does not reach past the card edge | Yes | No |
| 2 | The background shows software development, AI and machine learning motifs (code, neural network, binary) and the card text stays readable | Yes | No |
| 3 | `pytest`, `ruff` and `mypy --strict` pass and the application still has no runtime dependency except Flask | Yes | No |
| 4 | README and wiki (en, da, ms) describe the new background and show the regenerated screenshot | Yes | No |
| 5 | The code review against the `qc-programming` checklist for Python is a Go | Yes | No |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-003] | The screenshots, README and wiki exist and are updated here |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objective 2, personalised card | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in) |

## Target Date

2026-11-10

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Centre the portrait in the card | The 400 px portrait is wider than the card content, so it sits off centre and covers the horizontal line. Size the image to the card in the stylesheet, as the template does, and cover it by a test. | No | |
| 2 | Create the software development, AI and ML background | Generate a background image with code lines, a neural network and binary rows by a stdlib-only script under `tools/`, keep the template gradient so the card stays readable, and use it in the stylesheet. | No | |
| 3 | Regenerate the screenshot and update README and wiki | Re-run the Docker screenshot step for step 4 and update the README and the wiki pages in en, da and ms where they describe the background. | No | |
| 4 | Review the code and publish | Review against the Python checklist, write the `RC-*` record, open the pull request that closes the issues and merge it once the checks are green. | No | |

---

[BC-001]: ../business-case.md
[MIL-003]: ./mil-003-documentation.md
[29d7a1b]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/056-name-card/commit/29d7a1b6c94f38f99dc9162eab32b3b29f9c3374
