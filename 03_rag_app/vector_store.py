# STEP 3: Create vector embeddings using FAISS

from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from embeddings import get_chunks
from env import get_env_variable
import os

def get_vectorstore():
    embedding_model = OllamaEmbeddings(model=get_env_variable("EMBEDDING_MODEL_NAME"))
    vector_store_directory = get_env_variable("VECTOR_STORE_DIRECTORY")
    if os.path.isdir(vector_store_directory):
        # Load from disk
        vector_store = FAISS.load_local(vector_store_directory, embedding_model, allow_dangerous_deserialization=True)
        print("Vector store already exists.")
    else:
        print("Directory does not exist.")    
        chunks = get_chunks()
        vector_store = FAISS.from_documents(chunks, embedding=embedding_model)
        vector_store.save_local(vector_store_directory)
        print('AI book vector store is created using FAISS...')
    return vector_store