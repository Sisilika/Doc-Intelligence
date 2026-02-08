import streamlit as st
import json
import os

from backend.rag_pipeline import (
    load_document,
    chunk_documents,
    create_vector_store,
    retrieve_context
)

from backend.llm import ask_llm
from backend.extractor import extract_shipment_data


st.set_page_config(page_title="Doc Intelligence", layout="wide")

st.title("📄 Doc Intelligence")
st.write("Upload logistics documents, ask questions, or extract structured shipment data.")


UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

CONFIDENCE_THRESHOLD = 0.35


# -------------------
# Upload Section
# -------------------
st.header("📤 Upload Document")

uploaded_file = st.file_uploader("Upload PDF / DOCX / TXT", type=["pdf", "docx", "txt"])

if uploaded_file is not None:
    if st.button("Upload Document"):

        file_path = os.path.join(UPLOAD_DIR, uploaded_file.name)

        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())

        documents = load_document(file_path)
        chunks = chunk_documents(documents)
        create_vector_store(chunks)

        st.success("✅ Document uploaded and indexed!")


# -------------------
# Ask Question Section
# -------------------
st.header("❓ Ask Questions About Document")

question = st.text_input("Enter your question")

if st.button("Ask Question"):
    if question.strip() != "":

        context, sources, confidence = retrieve_context(question)

        if not context:
            st.error("Not found in document")
        else:

            prompt = f"""
Answer ONLY using this document context.

Context:
{context}

Question:
{question}
"""

            answer = ask_llm(prompt)

            if confidence < CONFIDENCE_THRESHOLD:
                answer = f"(Low confidence — verify manually)\n\n{answer}"

            st.subheader("Answer")
            st.write(answer)

            st.subheader("Confidence")
            st.write(confidence)

            st.subheader("Sources")
            st.json(sources)


# -------------------
# Extraction Section
# -------------------
st.header("📦 Structured Shipment Extraction")

if st.button("Run Extraction"):

    result = extract_shipment_data()

    st.subheader("Extracted Shipment Data")
    st.json(result)
