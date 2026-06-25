---
claim_id: claim-react-reasoning-action
claim_text: "Interleaving reasoning traces and grounded actions in LLM agents reduces task failure rates on multi-step knowledge-intensive benchmarks compared to chain-of-thought or action-only baselines."
status: supported
evidence_state: supported
source_references:
  - source-react-2023
primary_source_required: "yes"
review_notes: "ReAct paper shows consistent improvements over Act-only and CoT baselines on HotpotQA, FEVER, ALFWorld, and WebShop benchmarks."
paper_readiness: ready
---
# claim-react-reasoning-action

The ReAct paper demonstrates that combining verbal reasoning traces with executable actions yields consistent gains of 10–30% over both action-only and chain-of-thought (CoT) baselines on HotpotQA and FEVER question-answering tasks. On the interactive decision-making benchmarks ALFWorld and WebShop, ReAct agents recover from mid-trajectory errors by reading new observations and revising their plan, a capability unavailable to pure CoT agents that lack grounding in external feedback. These results directly support the claim that agent runtimes must implement a thought-action-observation loop: the runtime must capture each LLM-generated reasoning trace, dispatch the encoded action to the appropriate tool or environment, and reinject the resulting observation into the model's context before the next generation step. Without this loop, agents cannot dynamically correct mistakes and therefore fail more often on multi-step, knowledge-intensive tasks.
