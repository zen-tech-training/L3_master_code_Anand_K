# STEP 1: Load the external knowledgebase and convert into pages.
# Example - Knowledgebase in pdf format
from langchain_community.document_loaders import PyPDFLoader
from env import get_env_variable

def get_knowledgebase():
    loader = PyPDFLoader(get_env_variable("KNOWLEDGE_BASE_PATH"))
    pdf_pages = loader.load()
    print(f'No of pages: {len(pdf_pages)}')
    return pdf_pages