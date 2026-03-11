import streamlit as st
import chromadb

from chromadb.utils import embedding_functions

# Load embedding model
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

# Load Chroma database
client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="document_collection",
    embedding_function=embedding_function
)

st.title("📄 Audit Document Assistant")

st.write("Ask questions about auditing, governance, and compliance documents.")

query = st.text_input("Enter your question")

k = st.slider("Number of results", 1, 10, 3)

if st.button("Search"):

    results = collection.query(
        query_texts=[query],
        n_results=k
    )

    for i, doc in enumerate(results["documents"][0]):

        metadata = results["metadatas"][0][i]

        source = metadata.get("source", "Unknown")
        page = metadata.get("page", "N/A")

        st.subheader(f"Result {i+1}")
        st.write(f"Source: {source}")
        st.write(f"Page: {page}")
        st.write(doc)
        st.divider()