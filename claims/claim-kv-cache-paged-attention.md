---
claim_id: claim-kv-cache-paged-attention
claim_text: "PagedAttention partitions the KV cache memory into non-contiguous blocks to reduce fragmentation."
status: supported
evidence_state: supported
source_references:
  - source-kv-cache-2023
primary_source_required: "yes"
review_notes: "Key claim on memory fragmentation reduction."
paper_readiness: ready
---
# claim-kv-cache-paged-attention

PagedAttention resolves memory underutilization by managing the KV cache dynamically in memory.
