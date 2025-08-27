# 📚 Smart Librarian - AI Book Recommendation System

An intelligent AI chatbot that recommends books based on user interests using RAG (Retrieval-Augmented Generation) with ChromaDB and OpenAI GPT-4.

## 🎯 Features

# 📚 Smart Librarian

An AI-powered book recommendation system with a modern web interface and CLI, using Retrieval-Augmented Generation (RAG) with ChromaDB and OpenAI GPT-4.

---

## Features

- **Conversational AI Chatbot**: Get book recommendations and summaries via chat (web or CLI).
- **Semantic Search**: Uses ChromaDB and OpenAI embeddings for relevant book matching.
- **Tool Calling**: Fetches detailed book summaries on demand.
- **Content Filtering**: Detects and filters inappropriate language.
- **Modern Web UI**: Built with React, styled for clarity and responsiveness.
- **CLI Option**: Command-line interface for quick recommendations.
- **Romanian Language Support**: Optimized for Romanian queries and summaries.

---

## Project Structure

```
smart_librarian/
│
├── backend.py            # FastAPI server (API endpoints, CORS, health check)
├── main.py               # CLI entry point
├── requirements.txt      # Python dependencies
├── data/
│   └── book_summaries.txt
├── chroma_db/            # ChromaDB vector storage (auto-generated)
├── src/
│   ├── chatbot.py        # Main chatbot logic (OpenAI, RAG, CLI)
│   ├── tools.py          # Book summaries, content filter, tool definitions
│   ├── vector_store.py   # ChromaDB integration, semantic search
│   └── __init.py__.py
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── App.js, App.css, index.js, index.css, reportWebVitals.js
│   └── package.json
└── README.md
```

---

## Setup & Usage

### 1. Install Python dependencies

```powershell
python -m venv smart_librarian_env
smart_librarian_env\Scripts\activate
pip install -r requirements.txt
```

### 2. Set up environment

- Copy `.env.example` to `.env` and add your OpenAI API key.

### 3. Prepare data

- Ensure `data/book_summaries.txt` exists with book summaries.

### 4. Install and run the frontend

```powershell
cd frontend
npm install
npm start
```
Frontend runs at [http://localhost:3001](http://localhost:3001)

### 5. Start the backend

```powershell
cd ..
python backend.py
```
Backend runs at [http://localhost:8000](http://localhost:8000)

### 6. (Optional) Use CLI

```powershell
python main.py
```

---

## API Endpoints

- `GET /` — Health check
- `POST /chat` — Chat with the AI librarian (`{"message": "Vreau o carte despre prietenie"}`)
- `GET /books` — List all available books

---

## How it Works

- User asks for recommendations (web or CLI)
- Input is filtered for inappropriate language
- ChromaDB is queried for relevant books using OpenAI embeddings
- GPT-4 generates a conversational response, optionally calling a tool for a detailed summary
- The user receives recommendations and summaries

---

## Development

- **Backend (auto-reload):**
  ```powershell
  uvicorn backend:app --reload --host 0.0.0.0 --port 8000
  ```
- **Frontend (hot reload):**
  ```powershell
  cd frontend
  npm start
  ```

---

## Notes

- Requires an OpenAI API key in `.env`
- ChromaDB data is stored in `chroma_db/` (auto-generated)
- Frontend and backend must be run separately
- All book summaries are in `data/book_summaries.txt` and `src/tools.py`
- CORS is configured for ports 3000/3001

---

**Enjoy discovering new books with your AI librarian!**
### Port Configuration
- **Backend**: Runs on `http://localhost:8000`
- **Frontend**: Runs on `http://localhost:3001` (configurable via PORT environment variable)
- **CORS**: Backend accepts requests from ports 3001 and 3000 only

### File Dependencies
- Frontend depends on backend running on port 8000
- Backend depends on ChromaDB and OpenAI API key
- All imports and paths are configured for the manual file structure

### Troubleshooting
- If `.env` file doesn't work, set `OPENAI_API_KEY` as system environment variable
- CORS errors: Ensure backend is running and ports are correct
- Manifest errors: Create `frontend/public/manifest.json` with provided content
- Module not found: Run `pip install -r requirements.txt` in virtual environment

## 🔧 Troubleshooting

### Common Issues

**"OPENAI_API_KEY not found"**
- Ensure `.env` file exists with valid API key

**"Collection already exists"**
- Normal behavior - the system reuses existing data

**"Network connection error"**
- Check internet connection and API key validity

**"Books file not found"**
- Ensure `data/book_summaries.txt` exists

---

**Enjoy discovering new books with your AI librarian! 📚✨**