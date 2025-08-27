# 📚 Smart Librarian - AI Book Recommendation System

An intelligent AI chatbot that recommends books based on user interests using RAG (Retrieval-Augmented Generation) with ChromaDB and OpenAI GPT-4.

## 🎯 Features

- **RAG-powered Book Search**: Uses ChromaDB with OpenAI embeddings for semantic search
- **AI Chatbot**: Conversational interface powered by GPT-4
- **Tool Calling**: Detailed book summaries via OpenAI function calling
- **Content Filtering**: Basic inappropriate language detection
- **Multiple Interfaces**: Both CLI and Streamlit web interface
- **Romanian Language Support**: Optimized for Romanian interactions

## 🏗️ Architecture

```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   User Input    │───▶│  Vector Store   │───▶│   OpenAI GPT    │
│                 │    │   (ChromaDB)    │    │   + Function    │
└─────────────────┘    └─────────────────┘    │    Calling      │
                                              └─────────────────┘
                              │                         │
                              ▼                         ▼
                    ┌─────────────────┐    ┌─────────────────┐
                    │ Semantic Search │    │ Book Summaries  │
                    │   Results       │    │     Tool        │
                    └─────────────────┘    └─────────────────┘
```

## 📋 Requirements

- Python 3.8+
- Node.js 16+ and npm
- OpenAI API key
- Internet connection for API calls

## 🚀 Quick Start

### 1. Clone and Setup Project Structure

```bash
mkdir smart_librarian
cd smart_librarian
mkdir -p data src frontend
```

### 2. Setup Python Environment

```bash
# Create virtual environment
python -m venv smart_librarian_env

# Activate virtual environment
# Windows:
smart_librarian_env\Scripts\activate
# Mac/Linux:
source smart_librarian_env/bin/activate

# Install Python dependencies
pip install -r requirements.txt
```

### 3. Setup React Frontend

```bash
# Create React app directory
mkdir frontend
cd frontend

# Create all frontend files manually (see Frontend Files section below)
# After creating all files, install dependencies:
npm install

# The package-lock.json and node_modules/ will be auto-generated
```

**Important**: You need to create all the frontend files manually using the code provided in the "Frontend Files" section below.

### 4. Environment Setup

```bash
# Copy environment template
cp .env.example .env

# Edit .env and add your OpenAI API key
OPENAI_API_KEY=your_openai_api_key_here
```

### 5. Prepare Data

Ensure the `data/book_summaries.txt` file exists with the provided book summaries.

### 6. Run the Application

#### Option A: Full Stack Web Application (Recommended)

**Terminal 1 - Start Backend:**
```bash
python backend.py
```
Backend runs on: `http://localhost:8000`

**Terminal 2 - Start Frontend:**
```bash
cd frontend
npm start
```
Frontend runs on: `http://localhost:3000`

#### Option B: CLI Interface
```bash
python main.py
```

## 📁 Project Structure

```
smart_librarian/
├── data/
│   └── book_summaries.txt         # Book database (12 books)
├── src/
│   ├── vector_store.py            # ChromaDB integration
│   ├── tools.py                   # Function calling tools
│   ├── chatbot.py                 # Main chatbot logic
│   └── __init__.py
├── frontend/                      # React application
│   ├── public/
│   │   └── index.html             # Main HTML with loading screen
│   ├── src/
│   │   ├── App.js                 # Main React component
│   │   ├── App.css                # Component styles
│   │   ├── index.js               # React entry point
│   │   ├── index.css              # Global styles
│   │   └── reportWebVitals.js     # Performance monitoring
│   ├── package.json               # Node.js dependencies
│   ├── package-lock.json          # Auto-generated dependency lock
│   └── node_modules/              # Auto-generated packages
├── backend.py                     # FastAPI server
├── main.py                        # CLI entry point
├── requirements.txt               # Python dependencies
├── .env.example                   # Environment template
├── .env                           # Your API keys (create this)
├── .gitignore                     # Git ignore rules
└── README.md                      # This file
```

## 🔧 Core Components

### Backend Components

#### Vector Store (`vector_store.py`)
- Manages ChromaDB persistent storage
- Handles OpenAI embeddings creation
- Provides semantic search functionality
- Parses book summaries from text files

#### Tools (`tools.py`)
- `get_summary_by_title()`: Returns detailed book summaries
- Content filtering for inappropriate language
- OpenAI function calling integration

#### Chatbot (`chatbot.py`)
- Main conversation logic
- RAG implementation
- Tool calling orchestration
- User interface management

### Frontend Components

#### React App (`frontend/src/App.js`)
- Modern chat interface with real-time messaging
- Book browser sidebar
- Responsive design for all devices
- Loading states and error handling

#### FastAPI Backend (`backend.py`)
- RESTful API endpoints
- CORS configuration for React integration
- Async request handling
- Health monitoring

## 💬 Usage Examples

### Web Interface
1. Open `http://localhost:3000` in your browser
2. Type your book preferences in the chat
3. Get AI-powered recommendations with detailed summaries
4. Browse available books in the sidebar

### Basic Recommendations
```
You: Vreau o carte despre libertate și control social
AI: Îți recomand "1984" de George Orwell...
```

### Fantasy Books
```
You: Ce-mi recomanzi dacă iubesc poveștile fantastice?
AI: Pentru iubitorii de povești fantastice, îți recomand "The Hobbit"...
```

### Direct Book Inquiry
```
You: Ce este 1984?
AI: "1984" este un roman distopic scris de George Orwell...
```

## 📂 Frontend Files

You need to manually create all frontend files with the following content:

### `frontend/public/manifest.json`
```json
{
  "short_name": "Smart Librarian",
  "name": "Smart Librarian AI",
  "icons": [
    {
      "src": "favicon.ico",
      "sizes": "64x64 32x32 24x24 16x16",
      "type": "image/x-icon"
    }
  ],
  "start_url": ".",
  "display": "standalone",
  "theme_color": "#667eea",
  "background_color": "#ffffff"
}
```

### `frontend/public/index.html`
Create with the HTML code that includes loading screen and Google Fonts (see project artifacts).

### `frontend/src/index.js`
Create with React entry point code that handles loading screen (see project artifacts).

### `frontend/src/index.css`
Create with global CSS reset and styles (see project artifacts).

### `frontend/src/App.js`
Create with main React component featuring chat interface (see project artifacts).

### `frontend/src/App.css`
Create with component styles featuring glassmorphism design (see project artifacts).

### `frontend/src/reportWebVitals.js`
Create with performance monitoring code (see project artifacts).

**Note**: The complete code for each file is provided in the project artifacts. After creating all files, run `npm install` to generate `package-lock.json` and `node_modules/` automatically.

## 🛠️ Customization

### Adding More Books

1. Edit `data/book_summaries.txt`:
```
## Title: New Book Title
Short summary with main themes and plot points.
```

2. Add detailed summary to `tools.py`:
```python
book_summaries_dict["New Book Title"] = (
    "Detailed Romanian summary here..."
)
```

### Modifying Search Parameters

In `vector_store.py`, adjust:
```python
def search_books(self, query: str, n_results: int = 3):
    # Change n_results for more/fewer recommendations
```

### Content Filtering

In `tools.py`, modify the inappropriate words list:
```python
inappropriate_words = [
    # Add more words as needed
]
```

## 🔍 How It Works

1. **User Input**: User asks for book recommendations
2. **Content Filter**: Check for inappropriate language
3. **Semantic Search**: Query ChromaDB for relevant books
4. **AI Processing**: GPT-4 analyzes results and generates response
5. **Tool Calling**: If needed, fetch detailed summaries
6. **Response**: Present recommendations conversationally

## 📊 Database

The system includes 12 carefully curated books:
- 1984 (Dystopian)
- The Hobbit (Fantasy/Adventure)
- To Kill a Mockingbird (Literary Fiction)
- The Great Gatsby (American Literature)
- Harry Potter (Fantasy/Magic)
- Pride and Prejudice (Romance/Classic)
- The Lord of the Rings (Epic Fantasy)
- Dune (Science Fiction)
- The Catcher in the Rye (Coming of Age)
- Brave New World (Dystopian Sci-Fi)
- The Chronicles of Narnia (Children's Fantasy)
- One Hundred Years of Solitude (Magical Realism)

## 🚫 Error Handling

- **Missing API Key**: Clear error message with setup instructions
- **Network Issues**: Graceful degradation with retry suggestions
- **Invalid Queries**: Helpful guidance for better questions
- **Tool Failures**: Fallback responses when summaries aren't available
- **CORS Issues**: Properly configured for React development server

## 🎨 UI Features

### Web Interface Features:
✅ **Modern Design**: Clean interface with glassmorphism effects
✅ **Responsive Layout**: Optimized for desktop, tablet, and mobile
✅ **Real-time Chat**: Smooth messaging with typing indicators
✅ **Book Browser**: Expandable sidebar showing all available books
✅ **Message History**: Persistent chat history during session
✅ **Loading States**: Professional UX with visual feedback
✅ **Error Handling**: User-friendly error messages
✅ **Clear Chat**: Reset conversation anytime
✅ **Auto-scroll**: Messages automatically scroll to latest

### CLI Features:
✅ **Simple Commands**: Easy-to-use command-line interface
✅ **Colored Output**: Enhanced readability with emojis and formatting
✅ **Error Recovery**: Graceful handling of API failures
✅ **Exit Commands**: Multiple ways to quit (quit, exit, bye)

## 🛠️ API Endpoints

- `GET /`: Health check endpoint
- `POST /chat`: Send message to AI librarian
  ```json
  {
    "message": "Vreau o carte despre prietenie"
  }
  ```
- `GET /books`: Get list of all available books
  ```json
{
  "books": ["..."],
  "count": 12
}
```

## 🚀 Complete Setup Guide

### Step 1: Create Project Structure
```bash
mkdir smart_librarian
cd smart_librarian
mkdir -p data src frontend/public frontend/src
```

### Step 2: Python Backend Setup
```bash
# Create virtual environment
python -m venv smart_librarian_env

# Activate (Windows)
smart_librarian_env\Scripts\activate
# Activate (Mac/Linux)
source smart_librarian_env/bin/activate

# Install Python dependencies
pip install -r requirements.txt
```

### Step 3: Create Frontend Files
1. Create `frontend/package.json` with the content from the Frontend Files section above
2. Create all other frontend files (`index.html`, `App.js`, `App.css`, etc.) using the provided code
3. Create `frontend/public/manifest.json` (see Frontend Files section)
4. Install Node.js dependencies:
   ```bash
   cd frontend
   npm install
   # This auto-generates package-lock.json and node_modules/
   ```

### Step 4: Environment Configuration

**Option A: Environment Variable (Recommended)**
```bash
# Windows PowerShell - Set permanently for user
[System.Environment]::SetEnvironmentVariable('OPENAI_API_KEY', 'your_api_key_here', 'User')

# Or set for current session only
$env:OPENAI_API_KEY = "your_api_key_here"
```

**Option B: .env File**
```bash
# Create .env file in project root (same directory as backend.py)
echo OPENAI_API_KEY=your_api_key_here > .env
echo ENVIRONMENT=production >> .env

# Create frontend .env file (in frontend directory)
cd frontend
echo PORT=3001 > .env
echo REACT_APP_API_BASE_URL=http://localhost:8000 >> .env
```

**Important**: Replace `your_api_key_here` with your actual OpenAI API key.

### Step 5: Run the Application
```bash
# Terminal 1 - Backend (from project root)
# Set API key if not set permanently:
$env:OPENAI_API_KEY = "your_api_key_here"
python backend.py

# Terminal 2 - Frontend (from frontend directory)
cd frontend
npm start
```

Access the app at `http://localhost:3001`!

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Add your enhancements
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is for educational purposes. Ensure compliance with OpenAI's usage policies.

## 🔧 Development & Deployment

### Development Mode

**Backend Development:**
```bash
# Run with auto-reload
uvicorn backend:app --reload --host 0.0.0.0 --port 8000
```

**Frontend Development:**
```bash
cd frontend
npm start
# React dev server with hot reload on port 3000
```

### Production Build

**Frontend Build:**
```bash
cd frontend
npm run build
# Creates optimized build in frontend/build/
```

**Backend Deployment:**
```bash
# Install production ASGI server
pip install gunicorn
gunicorn backend:app -w 4 -k uvicorn.workers.UvicornWorker
```

## 🧩 Important Notes

### Environment Variables
- **OPENAI_API_KEY**: Required for OpenAI GPT-4 and embeddings API
- **.env file**: Should be in the same directory as `backend.py` (project root)
- **No quotes**: Environment variables in `.env` files should NOT have quotes around values
- **Alternative**: Set as system environment variable if `.env` file doesn't work

### Auto-Generated Files
- **`package-lock.json`**: Auto-generated when running `npm install` - **DO NOT create manually**
- **`node_modules/`**: Auto-generated package directory - **DO NOT commit to git**
- **`chroma_db/`**: Auto-generated by ChromaDB for vector storage

### Manual Setup Required
- All frontend source files must be created manually using the provided code
- React's `create-react-app` is **not used** in this setup
- Environment variables must be configured before running

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