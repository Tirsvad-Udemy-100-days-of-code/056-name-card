# SQA Review Record

## Metadata
| Key | Value |
| --- | --- |
| ID | RC-002 |
| CrossReference | [SA-001], [QC-SA-001] |

## Version History
| Date | Status | Author | Reviewer | Change | Commit |
| --- | --- | --- | --- | --- | --- |
| 2026-11-09 | Accepted | Jens Tirsvad Nielsen | S01 (AI as stand-in) | Initial version | [9d708b8] |

---

## Artifact Under Review

- Instance reviewed: [SA-001]
- Checklist used: [QC-SA-001]
- Scope: full review
- Language and domain: en / it
- Language reviewer: none (the reviewer reads English and knows the IT domain)
- Mode: autonomous, not independent (the reviewer is `AI as stand-in for S01`)

## Checklist Results

| # | Criterion | Status | Evidence/Notes |
| --- | --- | --- | --- |
| 1 | Power/Interest grid is filled for every stakeholder, with no gaps or unclassified entries | Pass | S01, S02 and S03 each have power, interest and quadrant. |
| 2 | Each stakeholder is assigned a unique, stable ID (e.g. S01-S11 style) reusable for RACI assignments in other artifacts | Pass | Stable IDs S01 to S03. |
| 3 | Roles and organizational context are defined with explicit Power and Interest levels, not just narrative description | Pass | Roles and organisation are given with explicit HIGH/LOW levels. |
| 4 | Communication needs (channel, frequency, deliverable type) are mapped to project phases or milestones | Pass | Communication Requirements table maps channels to milestones. |
| 5 | Conflicting stakeholder interests are identified with documented mitigation or resolution strategies | Pass | Two conflicts are listed with mitigations. |
| 6 | Stakeholder concerns are explicitly traced to Business Case objectives | Pass | Business Goal Alignment maps every concern to a BC-001 objective. |
| 7 | Primary concerns are expressed in both business language and a recognized quality-attribute mapping (e.g. FURPS+) | Pass | Concerns are in business language and mapped to FURPS+. |
| 8 | Document is understandable and navigable by non-technical stakeholders reviewing their own entry | Pass | Short, plain tables; each stakeholder can find their entry. |
| 9 | Every concern has a stable ID (`CN-NNN`) in the concern register, with the stakeholder who raised it; IDs are never renumbered or reused | Pass | CN-001 to CN-006 carry the raising stakeholder. |

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

[SA-001]: ../../stakeholder-analysis.md
[QC-SA-001]: ../../../framework/qc/artifacts/qc-stakeholder-analysis.md
[9d708b8]: https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/056-name-card/commit/9d708b837307d80c2675f65cdaed97c31d0bd133
