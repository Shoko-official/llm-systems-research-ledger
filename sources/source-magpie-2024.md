---
source_id: source-magpie-2024
title: "Magpie: Alignment Data Synthesis from Scratch by Prompting Aligned LLMs with Nothing"
authors: "Xu, Zhangchen and Jiang, Fengqing and Niu, Luyao and Deng, Yuntian and Poovendran, Radha and Choi, Yejin and Lin, Bill Yuchen"
year: 2024
source_type: paper
evidence_class: primary
venue: "arXiv preprint"
locator: "https://arxiv.org/abs/2406.08464"
review_notes: "Proposes generating alignment data by prompting an aligned LLM with only a pre-query template, allowing the model to self-generate diverse instruction-response pairs."
peer_reviewed: false
reliability_rating: high
---
# Magpie: Alignment Data Synthesis from Scratch by Prompting Aligned LLMs with Nothing

Magpie introduces a remarkably simple yet effective approach to alignment data synthesis: instead of crafting complex prompts or seed instructions, it feeds a chat-aligned LLM only the pre-query template (i.e., the system prompt prefix up to where the user turn would begin) and lets the model autoregressively complete both the user instruction and the assistant response. Because instruction-tuned models have strong priors about what a well-formed user query looks like, they spontaneously produce diverse, high-quality instruction–response pairs without any explicit guidance. Applied at scale to Llama-3 and Qwen-2, Magpie generates millions of alignment examples that, after quality filtering, match or outperform curated datasets like UltraChat and ShareGPT on AlpacaEval 2 and MT-Bench. The method demonstrates that a deployed aligned model implicitly encodes a rich distribution of human-like instructions that can be extracted for free, offering a low-cost, scalable alternative to red-teaming, crowd-sourcing, or elaborate prompt engineering for building alignment datasets.
