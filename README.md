# job-market-rag
An end-to-end RAG project that uses web scraping to collect job posts from job search platforms (linkedin, jobteaser ...) and use LLMs to extract the most relevant job based on different criterias

## Environment Setup

- **Manual (Windows PowerShell):**

	```powershell
	python -m venv .venv
	& .\.venv\Scripts\Activate.ps1
	python -m pip install --upgrade pip
	python -m pip install -r requirements.txt
	```

- **Notes:**
	- Edit `./.env` and fill real secret values. Do not commit the `.env` file to source control.
	- The `env_setup.ps1` script will create `.venv`, install `requirements.txt` (if present), and copy `.env.example` to `.env` if `.env` is missing.
