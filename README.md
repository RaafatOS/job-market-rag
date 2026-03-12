# job-market-rag
An end-to-end RAG project that uses web scraping to collect job posts from job search platforms (linkedin, jobteaser ...) and use LLMs to extract the most relevant job based on different criterias

## Environment Setup

- **Manual (Windows PowerShell):**

	```powershell
	python -m venv .venv
	& .\.venv\Scripts\Activate.ps1
	python -m pip install --upgrade pip
	python -m pip install -r requirements.txt
	Copy-Item .env.example .env
	```

- **Notes:**
	- Edit `./.env` and fill real secret values. Do not commit the `.env` file to source control.
	- Run `python ingestion/run_ingestion.py` before starting the CLI so the local FAISS index is created.

## Project Layout

- `app/`: interactive CLI entrypoint.
- `ingestion/`: text cleaning, chunking, embedding, and FAISS index creation.
- `rag/`: retriever, prompt, and question-answering flow.
- `data/processed/`: processed sample job data used by ingestion.

## Job Record Schema

Each scraped or hand-authored job should match this shape before ingestion:

- Required: `job_id`, `title`, `company`, `location`, `description`
- Optional: `url`, `source`, `posted_at`, `salary`, `tags`

The ingestion pipeline validates this contract in `ingestion/job_record.py`, which makes it a good target format for future scrapers.
