---
claim_id: claim-llm-span-retrieval-attribution
claim_text: "Hierarchical span structures isolate retrieval latency contribution from model generation latency in RAG pipelines."
status: supported
evidence_state: supported
source_references:
  - source-llm-agent-tracing-2024
  - source-dapper-2010
primary_source_required: "yes"
review_notes: "Differentiating retriever and LLM step spans allows localized profiling of slow operations."
paper_readiness: ready
---
# claim-llm-span-retrieval-attribution

Separate retrieval spans isolate bottlenecks in compound AI pipelines.
