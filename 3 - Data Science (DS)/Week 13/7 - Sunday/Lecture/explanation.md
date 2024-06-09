# RAG

You: In one paragraph, explain to me what RAG is in terms of machine learning
Assistant: RAG, or Retrieval-Augmented Generation, is an innovative approach in the field of machine learning that combines the strengths of information retrieval and text generation to enhance the accuracy and relevance of generated responses. The methodology integrates a retrieval component that searches a vast corpus of documents to find the most pertinent information related to a query, and then passes this information to a generative model, typically built on transformer architectures such as BERT or GPT. By leveraging retrieved documents, the generative model can produce more contextually accurate and informative answers, especially for queries requiring factual or detailed responses. This fusion allows RAG to effectively ground its responses in real-world data, bridging gaps between unsupervised text generation and knowledge retrieval systems.

- Retrieve specific documents
  - Documents will be vectorized (converted to vectors) and stored in what is known as a vector database
- Augment the prompt to the model (Prompt: What services does your company offer? Now you get relevant documents and send it along with the prompt to the model)
- Generate the response that is more accurate

# Fine-tuning

Train model further on specific data

- takes a long time
- requires a lot of compute
- have to retrain when adding new data each time

RAG, on the other hand

- dataset can be added to dynamically
- no extra training needed

Agentic RAG

- Uses RAG and agents (different models with different capabilities acting in one chain)
