# Audit RAG Assistant

This project is a document search assistant built using Retrieval-Augmented Generation (RAG) concepts.  
It allows users to ask questions about auditing and governance documents and retrieve the most relevant information.

The system uses SentenceTransformer embeddings and ChromaDB to perform semantic search over PDF and text documents.  
A Streamlit interface is used to interact with the system.

---

## Features

- Supports PDF and TXT documents
- Semantic search using SentenceTransformer embeddings
- Vector database using ChromaDB
- Document chunking for better retrieval
- Displays source document and page number
- Interactive web interface using Streamlit

---

## Project Structure

```
audit-rag-assistant
│
├── app.py
├── requirements.txt
├── rag_pipeline.ipynb
│
├── chroma_db
│
└── data
    ├── pdfs
    │     Internal-Audit-Framework-1.pdf
    │
    └── txt
          data_governance.txt
          market_analysis.txt
```

---

## Installation

1. Clone the repository.

```
git clone https://github.com/YOUR_USERNAME/audit-rag-assistant.git
cd audit-rag-assistant
```

2. Install the required libraries.

```
pip install -r requirements.txt
```

---

## Steps to Use the Project

1. Run the notebook to process the documents and create embeddings.

Open:

```
rag_pipeline.ipynb
```

Run all cells to:
- Load documents
- Chunk text
- Create embeddings
- Store vectors in ChromaDB

2. Run the Streamlit application.

```
streamlit run app.py
```

3. Open the browser and go to:

```
http://localhost:8500
```

4. Enter a question related to the documents.

Example questions:

```
What is internal auditing?
What is metadata management?
What is the purpose of audit reports?
```

The system will return the most relevant document sections along with the source file and page number.

---

## Technologies Used

- Python
- Streamlit
- ChromaDB
- Sentence Transformers
- LangChain utilities
- PyPDF

---

## Note

The application runs locally using Streamlit. The localhost URL may vary depending on the system configuration. Streamlit will display the correct URL in the terminal after running the application.

---

## Future Improvements

- Add LLM based answer generation
- Add chat style interface
- Allow users to upload documents
- Improve retrieval with hybrid search
