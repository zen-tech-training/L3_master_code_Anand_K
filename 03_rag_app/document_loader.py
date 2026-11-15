# STEP 1: Load the external knowledgebase and convert into pages.
# Example - Knowledgebase in pdf format
from langchain_community.document_loaders import PyPDFLoader

def get_knowledgebase():
    loader = PyPDFLoader("./knowledge_base/Artificial-Intelligence.pdf")
    pdf_pages = loader.load()
    print(f'No of pages: {len(pdf_pages)}')
    return pdf_pages