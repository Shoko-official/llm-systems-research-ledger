---
claim_id: claim-security-span-overhead-attribution
claim_text: "Dedicated security validation spans record policy filter evaluation latency to track safety overhead trends."
status: supported
evidence_state: supported
source_references:
  - source-llm-agent-tracing-2024
primary_source_required: "no"
review_notes: "Allows tracing of safety filter overhead independently of context assembly and model processing."
paper_readiness: ready
---
# claim-security-span-overhead-attribution

Logging safety filter latencies isolates compliance overhead from model execution.
