#!/usr/bin/env python3
"""
Smart Librarian - AI Chatbot with RAG + Tool Completion
Entry point for the application
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Add src to path
src_path = Path(__file__).parent / "src"
sys.path.append(str(src_path))


def setup_environment():
    """Setup environment variables and check requirements"""
    load_dotenv()

    # Check for required environment variables
    openai_api_key = os.getenv('OPENAI_API_KEY')
    if not openai_api_key:
        print("❌ OPENAI_API_KEY not found!")
        print("Please:")
        print("1. Copy .env.example to .env")
        print("2. Add your OpenAI API key to .env")
        print("3. Run the application again")
        sys.exit(1)

    # Check for required data files
    data_dir = Path(__file__).parent / "data"
    books_file = data_dir / "book_summaries.txt"

    if not books_file.exists():
        print(f"❌ Books file not found: {books_file}")
        print("Please ensure the data/book_summaries.txt file exists")
        sys.exit(1)

    return openai_api_key, books_file


def main():
    """Main entry point"""
    print("🚀 Starting Smart Librarian...")

    try:
        # Setup environment
        openai_api_key, books_file = setup_environment()

        # Import and start the chatbot
        from chatbot import SmartLibrarian

        librarian = SmartLibrarian(openai_api_key, str(books_file))
        librarian.start_chat()

    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("Please install required packages: pip install -r requirements.txt")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
        sys.exit(0)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()