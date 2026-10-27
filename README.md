# Local RAG Pipeline

a simple local Retrieval-Augmented Generation (RAG) pipeline for querying documents using a local LLM. this is just a personal project that i'm doing without any AI generated code so that i can force my brain to think its way through every part of the pipeline. so far its been pretty difficult but ive already learnt a lot and really enjoyed it.

## Features
- Semantic search your local files
- Works offline (as long as you have the models installed)

## How it works

1. Loads documents (currently only .txt files, will add more support soon) from `files/` directory
2. File contents are split into chunks (1000 char chunks with 200 char overflow)
3. Embedding model generated embeddings for each chunk and inserts a row (for each chunk) to the vectordb containing file metadata and the associated chunk vector
4. User inputs query using natural language
5. Embedding model retrieves relevant chunks
6. Local LLM generates an answer (todo)

## Tech Stack
- Python
- (llm to be decided, preferably something lightweight and performant)
- EmbeddingGemma2
- LanceDB

## Setup

todo