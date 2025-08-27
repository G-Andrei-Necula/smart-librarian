from fastapi import FastAPI, HTTPException, Request, Response
from pydantic import BaseModel
from contextlib import asynccontextmanager
import os
import sys
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
import uvicorn

# Add src to path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

try:
    from chatbot import SmartLibrarian
except ImportError:
    # Fallback import method
    import sys
    import importlib.util

    chatbot_path = src_path / "chatbot.py"
    spec = importlib.util.spec_from_file_location("chatbot", chatbot_path)
    chatbot_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(chatbot_module)
    SmartLibrarian = chatbot_module.SmartLibrarian

# Global librarian instance
librarian = None


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan handler"""
    global librarian

    openai_api_key = os.getenv('OPENAI_API_KEY')

    if not openai_api_key:
        raise RuntimeError("OPENAI_API_KEY not found in environment variables!")

    books_file = "data/book_summaries.txt"
    if not os.path.exists(books_file):
        raise RuntimeError(f"Books file not found: {books_file}")

    try:
        librarian = SmartLibrarian(openai_api_key, books_file)
        print("Smart Librarian initialized successfully!")
    except Exception as e:
        raise RuntimeError(f"Failed to initialize Smart Librarian: {e}")

    yield

    # Cleanup (if needed)
    print("Shutting down Smart Librarian...")


app = FastAPI(title="Smart Librarian API", version="1.0.0", lifespan=lifespan)


# Manual CORS handling middleware
@app.middleware("http")
async def cors_handler(request: Request, call_next):
    response = await call_next(request)

    # Get the origin from the request
    origin = request.headers.get("origin")

    # Allowed origins
    allowed_origins = [
        "http://localhost:3001",  # Main frontend port
        "http://localhost:3000",  # Backup port
    ]

    # Set CORS headers based on origin
    if origin in allowed_origins:
        response.headers["Access-Control-Allow-Origin"] = origin
        response.headers["Access-Control-Allow-Credentials"] = "true"
    else:
        response.headers["Access-Control-Allow-Origin"] = "http://localhost:3001"
        response.headers["Access-Control-Allow-Credentials"] = "false"

    response.headers["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response.headers["Access-Control-Allow-Headers"] = "*"

    return response


# Handle preflight OPTIONS requests
@app.options("/{path:path}")
async def handle_options(request: Request, path: str):
    origin = request.headers.get("origin")
    allowed_origins = [
        "http://localhost:3001",
        "http://localhost:3000",
    ]

    return Response(
        status_code=200,
        headers={
            "Access-Control-Allow-Origin": origin if origin in allowed_origins else "http://localhost:3001",
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Credentials": "true" if origin in allowed_origins else "false",
        }
    )


class ChatMessage(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str
    success: bool
    error: str = None


@app.get("/")
async def root():
    """Health check endpoint"""
    return {"message": "Smart Librarian API is running!", "status": "healthy"}


@app.post("/chat", response_model=ChatResponse)
async def chat(message: ChatMessage):
    """Chat endpoint for book recommendations"""
    if not librarian:
        raise HTTPException(status_code=500, detail="Smart Librarian not initialized")

    try:
        response = librarian.process_user_input(message.message)
        return ChatResponse(response=response, success=True)
    except Exception as e:
        return ChatResponse(
            response="A apărut o eroare în procesarea cererii tale. Te rog să încerci din nou.",
            success=False,
            error=str(e)
        )


@app.get("/books")
async def get_books():
    """Get list of available books"""
    if not librarian:
        raise HTTPException(status_code=500, detail="Smart Librarian not initialized")

    try:
        # Get all books from vector store
        results = librarian.vector_store.collection.get()
        books = []
        for i, metadata in enumerate(results['metadatas']):
            books.append({
                "id": results['ids'][i],
                "title": metadata['title'],
                "summary": results['documents'][i][:200] + "..." if len(results['documents'][i]) > 200 else
                results['documents'][i]
            })

        return {"books": books, "count": len(books)}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to get books: {str(e)}")


if __name__ == "__main__":
    uvicorn.run("backend:app", host="0.0.0.0", port=8000, reload=True)