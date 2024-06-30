# Corrective RAG (CRAG) for Document Retrieval

```
 ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
▐░█▀▀▀▀▀▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀▀▀ 
▐░▌          ▐░▌       ▐░▌▐░▌       ▐░▌▐░▌          
▐░▌          ▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌▐░▌ ▄▄▄▄▄▄▄▄ 
▐░▌          ▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░▌▐░░░░░░░░▌
▐░▌          ▐░█▀▀▀▀█░█▀▀ ▐░█▀▀▀▀▀▀▀█░▌▐░▌ ▀▀▀▀▀▀█░▌
▐░▌          ▐░▌     ▐░▌  ▐░▌       ▐░▌▐░▌       ▐░▌
▐░█▄▄▄▄▄▄▄▄▄ ▐░▌      ▐░▌ ▐░▌       ▐░▌▐░█▄▄▄▄▄▄▄█░▌
▐░░░░░░░░░░░▌▐░▌       ▐░▌▐░▌       ▐░▌▐░░░░░░░░░░░▌
 ▀▀▀▀▀▀▀▀▀▀▀  ▀         ▀  ▀         ▀  ▀▀▀▀▀▀▀▀▀▀▀ 
                   🦜🕸️ LangGraph   
                   🦜🔗 LangChain                                         
```
## Overview

This project implements the **[Corrective RAG (CRAG)](https://arxiv.org/pdf/2401.15884)** method for enhancing document retrieval and question answering. The CRAG method improves the retrieval-augmented generation process by evaluating the relevance of documents, transforming queries, and utilizing web searches for additional context.

This implementation leverages **🦜🕸️[LangGraph](https://langchain-ai.github.io/langgraph/)** for graph-based control flow management, **🦜🔗 [LangChain](https://python.langchain.com/v0.2/docs/introduction/)** for language model interactions, and **[Streamlit](https://streamlit.io/)** for creating a user-friendly web application interface.

## Features and Components 

- **Document Retrieval**: Retrieve relevant documents based on a user-provided question.
- **Document Grading**: Assess the relevance of documents to the question.
- **Query Transformation**: Improve the query to better retrieve relevant documents.
- **Web Search**: Perform web searches for additional context if needed.
- **Final Answer Generation**: Generate a final answer based on the retrieved documents and web search results.
- **Language Model**: `command-r-plus` by Cohere
- **Vector Store**: ChromaDB
- **Embedding Model**: `embed-english-light-v3.0` by Cohere

## Getting Started

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Kirouane-Ayoub/Corrective-RAG.git
   cd Corrective-RAG
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

- Models configurations are managed in `src/utils/settings.py`. Adjust the settings according to your environment and requirements.
- Create a .env file with the following content:

    ```
    COHERE_API_KEY=...
    ```
### Adding New Data

To add new documents to the knowledge base, place them in the `src/data_input` directory .

### Usage

- Run the app.py script using `streamlit` to start the Corrective-RAG pipeline:

   ```bash
   streamlit src/app.py
   ```
## Integration with LangSmith

You can integrate LangSmith for tracking your project by adding the following lines to your `.env` file:

```
LANGCHAIN_TRACING_V2=true
LANGCHAIN_ENDPOINT="https://api.smith.langchain.com"
LANGCHAIN_API_KEY="<your-api-key>"
```

### 🦜🛠️ LangSmith

**[LangSmith](https://python.langchain.com/v0.1/docs/langsmith/)**  is an all-in-one developer platform for every step of the LLM-powered application lifecycle, whether you’re building with LangChain or not. It allows you to debug, collaborate, test, and monitor your LLM applications effectively.
