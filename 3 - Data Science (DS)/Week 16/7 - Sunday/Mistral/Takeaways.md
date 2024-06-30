# Mixtral

Uses a "mixture of experts" architecture, meaning there are 8 feed forward neural networks known as "experts". When calling the model 2 of these experts are chosen and the average of their outputs is used to give an accurate prediction of the next token.

It is quite inexpensive, since it's a massive model, but only uses a subset of the model each time it's called.

## Open source models

Currently the 7B and 70B models are completely open source, and can be used for free. Mistral claims it outperforms Llama models at similar size.

Theyr SMoE model is also open source, and is a mixture of 8 experts. It outperforms or matches GPT-3.5 on most benchmarks.

It has 32k tokens context window.

They also have 3 embedding models, which are used to vectorize text as we've learned.

- [Mixtral Docs](https://docs.mistral.ai/getting-started/models/)

## Mistral API

- [Mistral API](https://docs.mistral.ai/getting-started/api/)
- [Quickstart](https://docs.mistral.ai/getting-started/quickstart/)
