# STEP 3: Create vector embeddings using FAISS

from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from embeddings import get_chunks
import os

def get_vectorstore():
    embedding_model = OllamaEmbeddings(model="nomic-embed-text")
    directory_path = "faiss_ai_book"
    if os.path.isdir(directory_path):
        # Load from disk
        vector_store = FAISS.load_local(directory_path, embedding_model, allow_dangerous_deserialization=True)
        print("Vector store already exists.")
    else:
        print("Directory does not exist.")    
        chunks = get_chunks()
        vector_store = FAISS.from_documents(chunks, embedding=embedding_model)
        vector_store.save_local("faiss_ai_book")
        print('AI book vector store is created using FAISS...')
    return vector_store