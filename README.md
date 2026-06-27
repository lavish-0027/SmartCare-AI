# SmartCare AI

Developed by Lavish Kumar — Built for Vibe2Ship Hackathon (Individual Participation)

SmartCare AI is a Retrieval-Augmented Generation (RAG) prototype that demonstrates a privacy-preserving, clinic-focused virtual assistant. It uses synthetic PDF content as a knowledge base, vector embeddings for retrieval, and a local or remote LLM to generate grounded, non-diagnostic responses.

## Problem Statement

Healthcare organizations often need accurate, clinic-specific information delivered to patients without exposing sensitive data or allowing LLM hallucinations. Developers need a safe way to prototype conversational assistants that rely on verified clinic content.

## Solution Overview

SmartCare AI ingests curated, synthetic clinic documents, indexes them into a vector store, and answers user queries by retrieving relevant passages and prompting an LLM with that context. The result is a grounded assistant that minimizes hallucination and preserves privacy.

## Features

- RAG-based retrieval from synthetic PDF knowledge base
- Context chunking and vector embeddings
- Lightweight Flask backend serving a `/chat` API
- Simple static frontend for quick demos
- Safety-first defaults and non-diagnostic disclaimers

## Tech Stack

- Python 3.8+
- Flask, Flask-CORS
- Transformers (Hugging Face) or remote HF Inference API
- scikit-learn / FAISS-style vector store
- Numpy, PyPDF for PDF processing

## Project Structure

- `backend/` — server, RAG logic, ingestion, and utilities
	- `app.py` — Flask server (serves `/chat`)
	- `answer_generator.py` — prompt building and response handling
	- `rag.py` — retrieval helper (alternate HF-based path)
	- `vector_store.py`, `ingest.py`, `pdf_loader.py` — data pipeline
- `frontend/` — static demo UI
	- `index.html`, `script.js`, `style.css`
- `data/` — synthetic PDF fixtures and generated artifacts
- `requirements.txt` — Python dependencies

## How to Run

1. Create a virtual environment and install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. (Optional) Set environment variables if using remote HF Inference API:

```powershell
setx HF_API_KEY "<your_hf_api_key>"
```

3. Start the backend server:

```powershell
python backend/app.py
```

4. Open the frontend demo in your browser:

Open `frontend/index.html` (double-click or use Live Server). The frontend will call `http://127.0.0.1:5000/chat` by default.

## Future Improvements

- Add authentication and role-based access control
- Integrate a production-grade vector DB (Chroma/FAISS/Annoy)
- Add multilingual content and voice UI
- Add automated tests and CI pipeline
- Improve UI/UX and accessibility

## Disclaimer

This application provides general, non-diagnostic healthcare assistance and does not replace professional medical advice. For emergencies or specific medical diagnoses, please consult a qualified healthcare provider.


 
