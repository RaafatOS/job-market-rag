from pathlib import Path

from dotenv import load_dotenv
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings

ROOT_DIR = Path(__file__).resolve().parent.parent
INDEX_PATH = ROOT_DIR / "faiss_index"


def load_retriever():
    load_dotenv()

    if not INDEX_PATH.exists():
        raise RuntimeError(
            "FAISS index not found. Run: python ingestion/run_ingestion.py"
        )

    db = FAISS.load_local(
        str(INDEX_PATH),
        OpenAIEmbeddings(),
        allow_dangerous_deserialization=True,
    )
    return db.as_retriever(search_kwargs={"k": 4})
