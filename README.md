# LLM Systems Research Ledger

`llm-systems-research-ledger` is the structured research tracking repository for the Modern LLM Systems 2026 / arXiv Report program.

This repository keeps research inputs auditable before they are used in the paper or in downstream prototypes. It is not a paper draft, retrieval system, citation formatter, benchmark, or source ingestion pipeline.

## Repository Role

This repository owns:

* source tracking conventions;
* claim tracking conventions;
* evidence status rules;
* citation readiness tracking;
* research TODO visibility;
* provenance and review rules for research materials.

The central project board is:

* [Modern LLM Systems 2026 / arXiv Report](https://github.com/users/Shoko-official/projects/4)

## Current Scope

Milestone 0 is limited to governance.

Included:

* governance documentation;
* issue and MR/PR templates;
* minimal validation commands;
* minimal CI;
* initial folder structure for ledger work.

Out of scope:

* real sources;
* real claims;
* citation datasets;
* BibTeX or Zotero import;
* scraping;
* search indexes;
* RAG;
* paper drafting.

## Evidence Policy

Every research claim must eventually have one of these evidence states:

* backed by a primary source;
* backed by a secondary source and marked for primary-source follow-up;
* explicitly marked `TODO:evidence_needed`;
* rejected or removed.

No unsupported claim should be treated as paper-ready.

## Source Policy

Primary sources are preferred for factual claims.

Examples of primary sources:

* papers;
* official technical reports;
* official product documentation;
* benchmark reports from the authors or maintainers of the benchmark;
* standards documents;
* source repositories for the system being discussed.

Secondary sources can be useful for discovery, but they should not be the final evidence for important claims unless a dedicated review accepts that limitation.

## Confidentiality

Do not commit:

* private notes not intended for the project;
* private datasets;
* credentials, tokens, cookies, or API keys;
* paid-access documents unless redistribution is explicitly allowed;
* copied paper text beyond short excerpts needed for fair reference;
* private correspondence.

## License

This repository is licensed under the Apache License 2.0. See [LICENSE](LICENSE).
