# STEP 2: Split the pages into chunks.
from langchain_text_splitters import RecursiveCharacterTextSplitter
from document_loader import get_knowledgebase

def get_chunks():
    pages = get_knowledgebase()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=30)
    chunks = text_splitter.split_documents(pages)
    print(f'No of chunks: {len(chunks)}')
    return chunks