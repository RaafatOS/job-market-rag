import json
from pathlib import Path

from ingestion.chunking import chunk_text
from ingestion.clean_text import clean_text
from ingestion.embed_and_store import build_vector_store
from ingestion.job_record import load_job_records

ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_PATH = ROOT_DIR / "data" / "processed" / "sample_job.json"
INDEX_PATH = ROOT_DIR / "faiss_index"


def main():
    if not DATA_PATH.exists():
        raise FileNotFoundError(f"Data file not found: {DATA_PATH}")

    with open(DATA_PATH, "r", encoding="utf-8") as f:
        jobs = load_job_records(json.load(f))

    all_chunks = []
    all_metadatas = []

    for job in jobs:
        cleaned_text = clean_text(job.text_for_embedding())
        chunks = chunk_text(cleaned_text)

        for chunk in chunks:
            all_chunks.append(chunk)
            all_metadatas.append(job.metadata())

    if not all_chunks:
        raise RuntimeError("No text chunks were generated. Check input data.")

    build_vector_store(all_chunks, all_metadatas)

    print(f"Ingestion complete - FAISS index saved to '{INDEX_PATH}'")


if __name__ == "__main__":
    main()
