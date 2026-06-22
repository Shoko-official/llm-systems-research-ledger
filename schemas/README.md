# Schemas

This directory contains the Draft-07 JSON schemas for validating the research ledger entities:

- **[source.json](file:///f:/Code/AI_ML/Article/Arxiv/llm-systems-research-ledger/schemas/source.json)**: Validates bibliographic sources, peer review status, and reliability.
- **[claim.json](file:///f:/Code/AI_ML/Article/Arxiv/llm-systems-research-ledger/schemas/claim.json)**: Validates atomic research assertions, their status, and evidence status.
- **[citation.json](file:///f:/Code/AI_ML/Article/Arxiv/llm-systems-research-ledger/schemas/citation.json)**: Validates citation mappings from sources/claims to paper sections.

All records in `sources/`, `claims/`, and `citations/` must conform to these schemas and are validated by the CI pipeline.
