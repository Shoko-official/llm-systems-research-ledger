---
claim_id: claim-evol-instruct-complexity
claim_text: "Iterative instruction evolution using LLMs as rewriters produces training data with systematically higher complexity, leading to improved performance on complex instruction-following tasks."
status: supported
evidence_state: supported
source_references:
  - source-evol-instruct-2023
primary_source_required: "yes"
review_notes: "WizardLM demonstrates models trained on Evol-Instruct data outperform base Alpaca and Vicuna models on complex instruction benchmarks."
paper_readiness: ready
---
# claim-evol-instruct-complexity

The WizardLM paper (Xu et al., ICLR 2023) provides controlled experimental evidence for this claim through both automated and human evaluation. Evol-Instruct applies two families of evolutionary operators to seed instructions: in-depth evolution (adding constraints, deepening specificity, increasing reasoning steps, complicating inputs) and in-breadth evolution (mutating topics to expand coverage). After multiple rounds of evolution and quality filtering, the resulting dataset contains a far greater proportion of high-complexity instructions than the Alpaca-52K baseline. A LLaMA model fine-tuned on this evolved corpus (WizardLM-7B) is preferred over Alpaca-7B in 71.8% of pairwise comparisons and over Vicuna-7B in 50.1% on a human evaluation set. Critically, the performance gap widens on the hardest difficulty tier of instructions (rated 8–10 out of 10), where WizardLM achieves the largest relative gains, directly supporting the claim that evolved data complexity translates to measurably better handling of complex instructions. This establishes Evol-Instruct as a principled, automated mechanism for controlling dataset difficulty in synthetic instruction tuning pipelines.
