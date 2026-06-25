---
source_id: source-self-instruct-2023
title: "Self-Instruct: Aligning Language Models with Self-Generated Instructions"
authors: "Wang, Yizhong and Kordi, Yeganeh and Mishra, Swaroop and Liu, Alisa and Smith, Noah A. and Khashabi, Daniel and Hajishirzi, Hannaneh"
year: 2023
source_type: paper
evidence_class: primary
venue: "Proceedings of the 61st Annual Meeting of the Association for Computational Linguistics"
locator: "https://arxiv.org/abs/2212.10560"
review_notes: "Proposes a pipeline to bootstrap instruction-following capabilities using GPT-3 generated instructions, enabling high-quality instruction tuning without human-curated datasets."
peer_reviewed: true
reliability_rating: high
---
# Self-Instruct: Aligning Language Models with Self-Generated Instructions

Self-Instruct introduces a fully automated pipeline that bootstraps an instruction-following language model from a small seed set of manually written task definitions. The method prompts a frozen GPT-3 model to generate new instruction–input–output triplets, applies a suite of filtering heuristics (ROUGE-L deduplication, classifier-based quality scoring, and length filtering) to remove low-quality or near-duplicate examples, and then fine-tunes a fresh model on the surviving synthetic data. Despite requiring no human annotation beyond the initial 175 seed tasks, a GPT-3 model fine-tuned on Self-Instruct data reaches roughly 90% of the performance of InstructGPT on the SUPERNI benchmark, and substantially outperforms the base model in human preference evaluations. This work is foundational for understanding how large-scale instruction datasets can be constructed without manual curation, directly informing the design of synthetic dataset generation pipelines used in modern LLM alignment workflows.
