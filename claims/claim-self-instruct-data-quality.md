---
claim_id: claim-self-instruct-data-quality
claim_text: "Instruction datasets generated via self-instruct pipelines using large LLMs match or exceed human-curated dataset quality on instruction-following benchmarks when filtered appropriately."
status: supported
evidence_state: supported
source_references:
  - source-self-instruct-2023
primary_source_required: "yes"
review_notes: "Self-Instruct paper shows GPT-3 self-generated data achieves ~90% of InstructGPT quality on SUPERNI benchmark."
paper_readiness: ready
---
# claim-self-instruct-data-quality

The Self-Instruct paper (Wang et al., ACL 2023) provides direct empirical evidence for this claim through a controlled comparison on the SUPERNI benchmark. A GPT-3 model fine-tuned exclusively on the synthetic instruction data produced by the Self-Instruct pipeline achieves roughly 90% of the performance of InstructGPT (which was trained with extensive human feedback via RLHF) on held-out SUPERNI tasks. Human preference evaluations further confirm that the Self-Instruct-tuned model is preferred over the raw GPT-3 baseline by a wide margin. The key enabling factor is the multi-stage filtering applied to the raw LLM outputs—ROUGE-L-based deduplication removes near-duplicate instructions, a binary classifier removes non-instruction-like generations, and length and keyword heuristics prune low-effort examples—demonstrating that quality filtering is essential for synthetic data to rival human-curated corpora. These results established that scalable, automated instruction dataset construction is a viable alternative to costly human annotation.
