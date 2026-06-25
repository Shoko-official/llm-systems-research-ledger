---
source_id: source-react-2023
title: "ReAct: Synergizing Reasoning and Acting in Language Models"
authors: "Yao, Shunyu and Zhao, Jeffrey and Yu, Dian and Du, Nan and Shafran, Izhak and Narasimhan, Karthik and Cao, Yuan"
year: 2023
source_type: paper
evidence_class: primary
venue: "International Conference on Learning Representations"
locator: "https://arxiv.org/abs/2210.03629"
review_notes: "Introduces ReAct framework that interleaves reasoning traces and task actions in LLM agents, showing significant improvements on knowledge-intensive and decision-making tasks."
peer_reviewed: true
reliability_rating: high
---
# ReAct: Synergizing Reasoning and Acting in Language Models

ReAct enables LLM agents to generate both verbal reasoning traces (thoughts) and task-specific actions in an interleaved manner, allowing the model to dynamically update its plan in response to external observations retrieved from tools or environments. This thought-action-observation loop is foundational to the agent runtime architecture described in the paper: the runtime must orchestrate the LLM's reasoning steps, dispatch the resulting action calls to external tools or APIs, and inject the resulting observations back into the model's context. By grounding reasoning in real-world feedback rather than relying solely on parametric knowledge, ReAct dramatically reduces hallucination-driven failures on multi-step tasks such as question answering over Wikipedia (HotpotQA) and fact verification (FEVER), as well as interactive decision-making benchmarks (ALFWorld, WebShop).
