from langchain_ollama import ChatOllama

def get_llm():
    llm = ChatOllama(model="llama3.2")
    return llm