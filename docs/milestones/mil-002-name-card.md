# Milestone 002 - Name card

## Metadata
| Key | Value |
| --- | --- |
| ID | MIL-002 |
| CrossReference | [BC-001] |
| Language | en |
| Domain | it |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | [9d708b8] |

---

## Purpose

Decide whether the Flask application serves the personalised name card at the root route, following the assignment's steps: download the template, create the Flask application, create `templates/` and `static/`, make `/` work, personalise.

## Deliverable

A Flask application in `src/` that renders the html5up Identity template at `/`, with the template assets in `static/`, the personalised text, links, photo and background image, the template attribution, and pytest tests for the route and the assets.

## Go / No-Go Criteria

| # | Criterion (objectively checkable) | Go | No-Go |
| --- | --- | --- | --- |
| 1 | `GET /` returns HTTP 200 and contains "Jens Tirsvad Nielsen" | Yes | No |
| 2 | Every `static/` URL in the rendered page returns HTTP 200 | Yes | No |
| 3 | The attribution to HTML5 UP (CCA 3.0) is on the page | Yes | No |
| 4 | `python -m pytest` exits 0 | Yes | No |
| 5 | The Python code review against `qc-programming-python` is a Go | Yes | No |

## Dependencies

| Depends on | Reason |
| --- | --- |
| [MIL-001] | The skeleton, configuration and tests must exist first |

## Traceability

| Business Case objective / KPI / user story | Reference |
| --- | --- |
| Objectives 1 and 2 | [BC-001] |
| Success criteria 1, 2 and 3 | [BC-001] |

## Ownership

| Role | Stakeholder ID (SA) |
| --- | --- |
| Owner | S01 |
| Approving reviewer | S01 (AI as stand-in) |

## Target Date

2026-11-12 — inside the one-week plan window.

## Tasks

| # | Task | Summary | Needs its own Use Case/User Story? | Reference |
| --- | --- | --- | --- | --- |
| 1 | Download the Identity template | Fetch the html5up Identity template and unpack it into a scratch folder to take its `index.html`, CSS, JavaScript, fonts and images; this is lecture step 1 of the final project. | No | |
| 2 | Create the Flask application and folders | Create the Flask server with `templates/` and `static/` folders and move the template files into them; lecture step 2. | No | |
| 3 | Serve the card at the root route | Render `index.html` with `render_template` at `/` and fix the asset paths to `static/`, so that the browser loads the CSS, scripts and images; lecture step 3. | No | |
| 4 | Personalise the card | Replace the name, text, links and photo with the data of S01 and the background image, and keep the HTML5 UP attribution; lecture step 4. | No | |
| 5 | Add route and asset tests | Add pytest tests that check `GET /` returns 200 with the name, that every `static/` URL on the page resolves and that the attribution is present. | No | |

---

[BC-001]: ../business-case.md
[MIL-001]: ./mil-001-scaffold.md
[9d708b8]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/056-name-card/commit/9d708b837307d80c2675f65cdaed97c31d0bd133
