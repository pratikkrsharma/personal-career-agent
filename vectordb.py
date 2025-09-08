import os
from pypdf import PdfReader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma


VECTORDB_PATH = "chroma_db"
EMBEDDING_MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"


def load_text_data():
    with open("me/Profile.txt", "r", encoding="utf-8") as f:
        profile_details = f.read()
    return profile_details


def create_vector_db():
    text = load_text_data()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_text(text)

    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
    db = Chroma.from_texts(chunks, embeddings, persist_directory=VECTORDB_PATH)
    db.persist()
    print("✅ Vector store updated.")
    return db


def load_vector_db():
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
    db = Chroma(persist_directory=VECTORDB_PATH, embedding_function=embeddings)
    return db


if __name__ == "__main__":
    create_vector_db()
