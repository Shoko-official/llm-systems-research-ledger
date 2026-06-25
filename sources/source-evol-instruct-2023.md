---
source_id: source-evol-instruct-2023
title: "WizardLM: Empowering Large Language Models to Follow Complex Instructions"
authors: "Xu, Can and Sun, Qingfeng and Zheng, Kai and Geng, Xiubo and Zhao, Pu and Feng, Jiazhan and Tao, Chongyang and Jiang, Daxin"
year: 2023
source_type: paper
evidence_class: primary
venue: "International Conference on Learning Representations"
locator: "https://arxiv.org/abs/2304.12244"
review_notes: "Introduces Evol-Instruct, a method that iteratively rewrites instructions to increase complexity using LLM-driven evolution, producing more challenging training examples."
peer_reviewed: true
reliability_rating: high
---
# WizardLM: Empowering Large Language Models to Follow Complex Instructions

WizardLM introduces Evol-Instruct, an automatic dataset augmentation technique in which ChatGPT is used as an evolver to iteratively rewrite an initial pool of seed instructions into progressively harder variants. The evolver applies two families of mutation operators: in-depth evolution (deepening constraints, concretizing vague concepts, adding reasoning steps, and increasing input complexity) and in-breadth evolution (generating topically diverse new instructions). Each evolved instruction is validated for quality, and surviving examples are collected into a training corpus that contains far more complex and varied instructions than the original Alpaca or ShareGPT datasets. A LLaMA model fine-tuned on this corpus—WizardLM—outperforms Alpaca and Vicuna on human evaluation across difficulty-stratified subsets, with especially large margins on the hardest instruction categories. The work demonstrates that systematic, automated control over instruction complexity is both feasible and highly effective, establishing Evol-Instruct as a widely adopted building block in synthetic dataset generation pipelines for LLM instruction tuning.
