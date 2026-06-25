---
source_id: source-toolformer-2023
title: "Toolformer: Language Models Can Teach Themselves to Use Tools"
authors: "Schick, Timo and Dwivedi-Yu, Jane and Dessi, Roberto and Raileanu, Roberta and Lomeli, Maria and Hambro, Eric and Zettlemoyer, Luke and Cancedda, Nicola and Scialom, Thomas"
year: 2023
source_type: paper
evidence_class: primary
venue: "Advances in Neural Information Processing Systems"
locator: "https://arxiv.org/abs/2302.04761"
review_notes: "Demonstrates that LLMs can be trained to decide when and how to call external APIs without sacrificing language modeling capabilities."
peer_reviewed: true
reliability_rating: high
---
# Toolformer: Language Models Can Teach Themselves to Use Tools

Toolformer introduces a self-supervised pipeline in which a language model first proposes candidate API call annotations for its own training corpus, filters those candidates by whether they actually reduce future prediction loss, and then fine-tunes on the surviving examples. This bootstrapping process teaches the model to invoke a diverse set of external tools—including a calculator, a calendar, a Wikipedia search engine, a machine translation API, and a question-answering system—sparingly and only when it would genuinely help. The resulting model uses tools in zero-shot settings without any task-specific prompting, and it outperforms much larger models on numerical reasoning and knowledge retrieval while maintaining competitive performance on standard language-modeling benchmarks. These findings directly ground the tool-call routing and API integration component of LLM agent runtimes, demonstrating that tool selection and invocation can be learned end-to-end rather than hardcoded by the runtime developer.
