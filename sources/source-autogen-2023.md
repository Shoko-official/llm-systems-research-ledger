---
source_id: source-autogen-2023
title: "AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation"
authors: "Wu, Qingyun and Bansal, Gagan and Zhang, Jieyu and Wu, Yiran and Zhang, Shaokun and Zhu, Erkang and Li, Beibin and Jiang, Li and Zhang, Xiaoyun and Wang, Chi"
year: 2023
source_type: paper
evidence_class: primary
venue: "arXiv preprint"
locator: "https://arxiv.org/abs/2308.08155"
review_notes: "Introduces AutoGen framework for building multi-agent LLM applications via structured conversation between customizable agents."
peer_reviewed: false
reliability_rating: high
---
# AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation

AutoGen defines a conversable agent abstraction in which each agent encapsulates an LLM backend, a set of executable skills (code execution, tool calls, human input), and a conversation history. Agents interact by sending and receiving messages within a shared conversational loop, and the framework supports flexible topologies including two-agent dialogues, dynamic group chats with a facilitator, and nested or hierarchical agent compositions. This design separates the orchestration logic (who talks to whom, and when) from the individual agent capabilities, making it straightforward to compose specialized agents—a planner, a coder, an executor, and a critic—into a pipeline that can decompose complex tasks, catch errors through agent-to-agent feedback, and optionally route decisions to a human in the loop. AutoGen's multi-agent conversation patterns directly underpin the coordination architecture referenced in the agent runtime section, providing empirical evidence that structured message passing between LLM agents outperforms single-agent baselines on coding, mathematical reasoning, and decision-making benchmarks.
