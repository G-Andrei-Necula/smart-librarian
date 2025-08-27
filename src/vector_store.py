import chromadb
from chromadb.config import Settings
import openai
import os
from typing import List, Dict
import re


class BookVectorStore:
    def __init__(self, openai_api_key: str, persist_directory: str = "./chroma_db"):
        self.openai_client = openai.Client(api_key=openai_api_key)
        self.chroma_client = chromadb.PersistentClient(path=persist_directory)
        self.collection = None

    def create_collection(self, collection_name: str = "books"):
        """Create or get existing collection"""
        try:
            self.collection = self.chroma_client.get_collection(collection_name)
            print(f"Collection '{collection_name}' already exists with {self.collection.count()} documents")
        except:
            self.collection = self.chroma_client.create_collection(collection_name)
            print(f"Created new collection '{collection_name}'")

    def get_embeddings(self, texts: List[str]) -> List[List[float]]:
        """Get embeddings from OpenAI"""
        response = self.openai_client.embeddings.create(
            model="text-embedding-3-small",
            input=texts
        )
        return [data.embedding for data in response.data]

    def parse_books_file(self, file_path: str) -> List[Dict]:
        """Parse the book summaries file"""
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        books = []
        book_sections = re.split(r'## Title: ', content)[1:]  # Skip empty first element

        for section in book_sections:
            lines = section.strip().split('\n', 1)
            if len(lines) >= 2:
                title = lines[0].strip()
                summary = lines[1].strip()
                books.append({
                    'title': title,
                    'summary': summary,
                    'full_text': f"Title: {title}\n{summary}"
                })

        return books

    def populate_database(self, books_file_path: str):
        """Load books into ChromaDB"""
        if self.collection.count() > 0:
            print("Database already populated. Skipping...")
            return

        books = self.parse_books_file(books_file_path)
        print(f"Parsed {len(books)} books from file")

        texts = [book['full_text'] for book in books]
        embeddings = self.get_embeddings(texts)

        ids = [f"book_{i}" for i in range(len(books))]
        metadatas = [{'title': book['title']} for book in books]
        documents = [book['summary'] for book in books]

        self.collection.add(
            embeddings=embeddings,
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )

        print(f"Added {len(books)} books to vector database")

    def search_books(self, query: str, n_results: int = 3) -> List[Dict]:
        """Search for books using semantic similarity"""
        query_embedding = self.get_embeddings([query])[0]

        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )

        books_found = []
        for i in range(len(results['ids'][0])):
            books_found.append({
                'title': results['metadatas'][0][i]['title'],
                'summary': results['documents'][0][i],
                'distance': results['distances'][0][i] if 'distances' in results else 0
            })

        return books_found