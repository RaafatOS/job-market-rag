from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

def load_retriever():
    db = FAISS.load_local(
        "faiss_index",
        OpenAIEmbeddings(),
        allow_dangerous_deserialization=True
    )
    return db.as_retriever(search_kwargs={"k": 4})
