from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

def build_vector_store(chunks, metadatas):
    load_dotenv()
    embeddings = OpenAIEmbeddings()
    vector_db = FAISS.from_texts(
        texts=chunks,
        embedding=embeddings,
        metadatas=metadatas
    )
    vector_db.save_local("faiss_index")
