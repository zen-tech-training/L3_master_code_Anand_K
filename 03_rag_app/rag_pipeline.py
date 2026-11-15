# STEP 4: Build Retrieval Chain

from langchain_core.prompts import PromptTemplate
from langchain_classic.chains import RetrievalQA
from llm import get_llm
from vector_store import get_vectorstore

def get_rag_pipeline():
    llm = get_llm()
    vector_store = get_vectorstore()
    USER_PROMPT_TEMPLATE = """Use the following pieces of the context to answer user's question.
    If you don't know the answer, just say you don't know, don't try to make up the answer.
    ------------------------
    {context}
    Question: {question}
    """

    USER_PROMPT = PromptTemplate(
        template=USER_PROMPT_TEMPLATE,
        input_variables=["context", "question"]
    )
    retriever = vector_store.as_retriever()
    qa_chain = RetrievalQA.from_chain_type(
        llm,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": USER_PROMPT}
    )
    return retriever, qa_chain

