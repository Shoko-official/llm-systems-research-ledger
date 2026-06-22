---
claim_id: claim-tracing-context-propagation-overhead
claim_text: "Injecting and extracting W3C trace context headers adds less than 1 millisecond of processing latency per HTTP request."
status: supported
evidence_state: supported
source_references:
  - source-opentelemetry-2023
  - source-dapper-2010
primary_source_required: "yes"
review_notes: "Ensures tracing context overhead is minimal for HTTP gateways and service requests."
paper_readiness: ready
---
# claim-tracing-context-propagation-overhead

W3C Trace Context propagation introduces negligible latency.
