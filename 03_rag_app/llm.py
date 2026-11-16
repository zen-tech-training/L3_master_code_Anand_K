from langchain_ollama import ChatOllama
import os
from dotenv import load_dotenv, find_dotenv
from env import get_env_variable

def get_llm():
    llm = ChatOllama(model=get_env_variable("MODEL_NAME"))
    return llm