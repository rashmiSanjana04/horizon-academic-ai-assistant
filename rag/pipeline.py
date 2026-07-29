"""
rag/pipeline.py

Handles:
- Loading policy documents from the data/ folder
- Splitting them into chunks
- Creating/loading a Chroma vector store with Google Gemini embeddings (free tier)
"""

from pathlib import Path

from dotenv import load_dotenv

load_dotenv()  # Load GOOGLE_API_KEY from .env

from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma

DATA_DIR = Path(__file__).resolve().parent.parent / "data"
VECTOR_STORE_DIR = Path(__file__).resolve().parent.parent / "vector_store"


def get_embeddings():
    """Google Gemini embedding model - free tier, no billing required."""
    return GoogleGenerativeAIEmbeddings(model="models/gemini-embedding-001")


def load_documents():
    """Load all .md/.txt policy documents from the data/ folder."""
    documents = []
    for file_path in DATA_DIR.glob("*.md"):
        loader = TextLoader(str(file_path), encoding="utf-8")
        documents.extend(loader.load())
    return documents


def split_documents(documents):
    """Split documents into overlapping chunks suitable for embedding."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150,
        separators=["\n## ", "\n### ", "\n\n", "\n", " ", ""],
    )
    return splitter.split_documents(documents)


def build_vector_store():
    """Build (or rebuild) the Chroma vector store from the policy documents."""
    documents = load_documents()
    if not documents:
        raise ValueError(
            f"No documents found in {DATA_DIR}. Add .md policy files first."
        )

    chunks = split_documents(documents)
    embeddings = get_embeddings()

    vector_store = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(VECTOR_STORE_DIR),
        collection_name="horizon_academic_policies",
    )
    print(f"Vector store built with {len(chunks)} chunks from {len(documents)} documents.")
    return vector_store


def load_vector_store():
    """Load an existing Chroma vector store, or build one if it doesn't exist."""
    embeddings = get_embeddings()

    if VECTOR_STORE_DIR.exists() and any(VECTOR_STORE_DIR.iterdir()):
        return Chroma(
            persist_directory=str(VECTOR_STORE_DIR),
            embedding_function=embeddings,
            collection_name="horizon_academic_policies",
        )
    return build_vector_store()


if __name__ == "__main__":
    # Run this file directly to (re)build the vector store:
    # python -m rag.pipeline
    build_vector_store()