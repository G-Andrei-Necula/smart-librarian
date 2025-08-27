import openai
import json
from typing import List, Dict, Optional
from vector_store import BookVectorStore
from tools import get_summary_by_title, get_summary_tool_definition, filter_inappropriate_language


class SmartLibrarian:
    def __init__(self, openai_api_key: str, books_file_path: str):
        self.openai_client = openai.Client(api_key=openai_api_key)
        self.vector_store = BookVectorStore(openai_api_key)
        self.books_file_path = books_file_path

        # Initialize vector store
        self.vector_store.create_collection()
        self.vector_store.populate_database(books_file_path)

        # System prompt
        self.system_prompt = """
        Ești un bibliotecar AI inteligent și prietenos care recomandă cărți utilizatorilor în funcție de interesele lor.

        Când un utilizator îți cere o recomandare de carte:
        1. Analizează cererea și identifică temele, genurile sau preferințele
        2. Caută în baza ta de date de cărți folosind informațiile furnizate
        3. Recomandă una dintre cărțile găsite
        4. Folosește tool-ul get_summary_by_title pentru a obține un rezumat detaliat
        5. Prezintă recomandarea într-un mod conversațional și prietenos

        Răspunde în română și fii entuziasmant când faci recomandări!
        """

        self.tools = [get_summary_tool_definition]

    def search_and_recommend(self, user_query: str) -> List[Dict]:
        """Search for relevant books based on user query"""
        return self.vector_store.search_books(user_query, n_results=3)

    def chat_completion(self, messages: List[Dict], use_tools: bool = True):
        """Get chat completion from OpenAI with optional tool calling"""
        params = {
            "model": "gpt-4",
            "messages": messages,
            "temperature": 0.7,
            "max_tokens": 1500
        }

        if use_tools:
            params["tools"] = self.tools
            params["tool_choice"] = "auto"

        return self.openai_client.chat.completions.create(**params)

    def handle_tool_calls(self, tool_calls):
        """Handle function calls from the assistant"""
        tool_results = []

        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_args = json.loads(tool_call.function.arguments)

            if function_name == "get_summary_by_title":
                result = get_summary_by_title(function_args["title"])
                tool_results.append({
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": result
                })

        return tool_results

    def process_user_input(self, user_input: str) -> str:
        """Process user input and return response"""
        # Filter inappropriate language
        is_appropriate, filtered_message = filter_inappropriate_language(user_input)
        if not is_appropriate:
            return filtered_message

        # Search for relevant books
        relevant_books = self.search_and_recommend(user_input)

        # Prepare context with found books
        books_context = "Cărți relevante găsite:\n"
        for i, book in enumerate(relevant_books, 1):
            books_context += f"{i}. {book['title']}: {book['summary']}\n"

        # Prepare messages for chat completion
        messages = [
            {"role": "system", "content": self.system_prompt},
            {"role": "system", "content": f"Context: {books_context}"},
            {"role": "user", "content": user_input}
        ]

        # Get initial response
        response = self.chat_completion(messages)
        assistant_message = response.choices[0].message

        # Handle tool calls if any
        if assistant_message.tool_calls:
            messages.append({
                "role": "assistant",
                "content": assistant_message.content,
                "tool_calls": [
                    {
                        "id": tc.id,
                        "type": tc.type,
                        "function": {
                            "name": tc.function.name,
                            "arguments": tc.function.arguments
                        }
                    } for tc in assistant_message.tool_calls
                ]
            })

            # Get tool results
            tool_results = self.handle_tool_calls(assistant_message.tool_calls)
            messages.extend(tool_results)

            # Get final response with tool results
            final_response = self.chat_completion(messages)
            return final_response.choices[0].message.content

        return assistant_message.content

    def start_chat(self):
        """Start the CLI chat interface"""
        print("🤖 Bună! Sunt bibliotecarul tău AI. Îți pot recommanda cărți în funcție de interesele tale!")
        print("💡 Exemple de întrebări:")
        print("   - 'Vreau o carte despre libertate și control social'")
        print("   - 'Ce-mi recomanzi dacă iubesc poveștile fantastice?'")
        print("   - 'Ce este 1984?'")
        print("📝 Scrie 'quit' pentru a ieși\n")

        while True:
            try:
                user_input = input("Tu: ").strip()

                if user_input.lower() in ['quit', 'exit', 'bye']:
                    print("📚 La revedere! Sper că îți vor plăcea cărțile recomandate!")
                    break

                if not user_input:
                    continue

                print("🤔 Caut cele mai potrivite cărți pentru tine...")
                response = self.process_user_input(user_input)
                print(f"\n📖 Bibliotecarul AI: {response}\n")
                print("-" * 80)

            except KeyboardInterrupt:
                print("\n\n📚 La revedere!")
                break
            except Exception as e:
                print(f"❌ A apărut o eroare: {e}")
                print("Te rog să încerci din nou.")


def main():
    import os
    from dotenv import load_dotenv

    load_dotenv()

    openai_api_key = os.getenv('OPENAI_API_KEY')
    if not openai_api_key:
        print("❌ Te rog să setezi OPENAI_API_KEY în fișierul .env")
        return

    books_file = "data/book_summaries.txt"
    if not os.path.exists(books_file):
        print(f"❌ Fișierul {books_file} nu există!")
        return

    try:
        librarian = SmartLibrarian(openai_api_key, books_file)
        librarian.start_chat()
    except Exception as e:
        print(f"❌ Eroare la inițializarea bibliotecii: {e}")


if __name__ == "__main__":
    main()