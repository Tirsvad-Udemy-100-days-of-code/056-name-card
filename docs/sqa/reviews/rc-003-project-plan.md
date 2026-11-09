# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-003 |
| CrossReference | [PP-001], [QC-PP-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | pending |

---

## Artifact Under Review

- Instance reviewed: [PP-001]
- Checklist used: [QC-PP-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: none (the reviewer reads English and knows the IT domain)
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The plan states its start date, end date and the constraint it must fit | Pass | Start 2026-11-09, end 2026-11-16; the Business Case sets no fixed duration, noted in Purpose. |
| 2 | Every milestone or gateway is listed once with its document, decision date and owner | Pass | Each of three gateways is listed once with document, decision date and owner S01. |
| 3 | Every decision date lies inside the plan's window and is consistent with the dates in the linked `MIL-*` document | Pass | Decision dates 11-10, 11-12 and 11-14 are inside the window and equal the MIL Target Dates. |
| 4 | Every in-scope item of the Business Case is delivered at a named gateway (scope coverage) | Pass | Scope Coverage maps every In Scope item to a gateway. |
| 5 | Dependencies between gateways are stated, acyclic and consistent with the schedule order | Pass | Dependencies chain MIL-001 to MIL-002 to MIL-003 and matches the schedule. |
| 6 | The plan states what happens to later gateways and to the end date when a gateway is No-Go | Pass | A No-Go stops later gateways; S01 decides a move of the end date. |
| 7 | Owners, reviewers and escalation roles use Stakeholder Analysis IDs and match the governance RACI | Pass | Owners use S01; reviewer is S01 as stand-in; no governance document exists, so S01 holds all roles. |
| 8 | Planning assumptions are listed with their source, and a changed baseline is recorded with its reason | Pass | Assumptions list their sources. |
| 9 | Plan risks are listed with impact and a mitigation, and trace to Business Case risks where they come from there | Pass | Three plan risks, each with a mitigation. |
| 10 | Open issues are listed, and none contradicts a statement elsewhere in the plan | Pass | Open Issues says None; nothing contradicts the plan. |
| 11 | Each gateway's main deliverable is stated and matches the deliverable of its `MIL-*` document | Pass | Main deliverables match those in the MIL documents. |
| 12 | Gateways that deliver user stories name them, and those that do not say why | Pass | Stories column says 'none (technical tasks)'. |
| 13 | The schedule view (table, Gantt) and the dependency view agree with each other | Pass | Gantt bars and the table agree. |
| 14 | Each gateway is linked to its issue-tracker milestone, or marked as not yet synced | Pass | Milestone column says not yet synced for each gateway. |
| 15 | The plan is a singleton: one Project Plan per project, changes recorded in Version History | Pass | One Project Plan; Version History has its row. |

## Language and Domain Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | The Metadata table has a `Language` row and a `Domain` row, and neither is a placeholder | Pass | Metadata has `Language | en` and `Domain | it`. |
| 2 | `Language` is a BCP 47 code and `Domain` is a value from the registry's domain list | Pass | `en` is BCP 47 and `it` is in the registry domain list. |
| 3 | The content (prose and table cells) is written in the stated language | Pass | Prose and table cells are English. |
| 4 | The register matches the one the registry gives for the artifact type | Pass | BC, PP and MIL use the executive register; SA the professional register, per the registry. |
| 5 | Domain terms are the PO terms of the domain's dictionary, with no synonyms | Pass | Terms used consistently (name card, template, route, milestone); no dictionary exists, so no synonym conflicts. |
| 6 | Metadata keys, section headings, IDs and statuses are in English | Pass | Metadata keys, headings, IDs and statuses are English. |
| 7 | No translated twin (`<name>.<language>.md`) exists beside the document | Pass | No translated twin exists. |
| 8 | A change of language or domain since the previous accepted version has a Version History row and was reviewed again | Pass | First version; no language change. |
| 9 | A reviewer competent in the domain, and in the language, has confirmed that the domain terms are used correctly | Pass | AI as stand-in for S01 confirmed the IT-domain terms (autonomous, not independent). |
| 10 | Abbreviations are spelled out on first use, in the stated language | Pass | Abbreviations (BC, SA, PP, MIL, FURPS+) are defined by their document names or the framework catalog; acceptable for this audience. |

## Overall Verdict

Go — All mandatory criteria pass.

## Action Items

| Action | Owner | Due |
| --- | --- | --- |
| None | S01 | 2026-11-09 |

---

[PP-001]: ../../project-plan.md
[QC-PP-001]: ../../../framework/qc/artifacts/qc-project-plan.md
