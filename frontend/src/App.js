import React, { useState, useEffect, useRef } from 'react';
import axios from 'axios';
import './App.css';

const API_BASE_URL = 'http://localhost:8000';

function App() {
  const [messages, setMessages] = useState([]);
  const [inputMessage, setInputMessage] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [books, setBooks] = useState([]);
  const [showBooks, setShowBooks] = useState(false);
  const messagesEndRef = useRef(null);

  useEffect(() => {
    // Add welcome message
    setMessages([
      {
        id: 1,
        role: 'assistant',
        content: `🤖 Bună! Sunt bibliotecarul tău AI. Îți pot recommanda cărți în funcție de interesele tale!

💡 **Exemple de întrebări:**
• 'Vreau o carte despre libertate și control social'
• 'Ce-mi recomanzi dacă iubesc poveștile fantastice?'
• 'Ce este 1984?'`,
        timestamp: new Date()
      }
    ]);

    // Fetch available books
    fetchBooks();
  }, []);

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  const fetchBooks = async () => {
    try {
      const response = await axios.get(`${API_BASE_URL}/books`);
      setBooks(response.data.books);
    } catch (error) {
      console.error('Failed to fetch books:', error);
    }
  };

  const sendMessage = async (e) => {
    e.preventDefault();
    if (!inputMessage.trim() || isLoading) return;

    const userMessage = {
      id: Date.now(),
      role: 'user',
      content: inputMessage,
      timestamp: new Date()
    };

    setMessages(prev => [...prev, userMessage]);
    setInputMessage('');
    setIsLoading(true);

    try {
      const response = await axios.post(`${API_BASE_URL}/chat`, {
        message: inputMessage
      });

      const assistantMessage = {
        id: Date.now() + 1,
        role: 'assistant',
        content: response.data.response,
        timestamp: new Date()
      };

      setMessages(prev => [...prev, assistantMessage]);
    } catch (error) {
      const errorMessage = {
        id: Date.now() + 1,
        role: 'assistant',
        content: '❌ A apărut o eroare în comunicarea cu serverul. Te rog să încerci din nou.',
        timestamp: new Date()
      };
      setMessages(prev => [...prev, errorMessage]);
      console.error('Chat error:', error);
    } finally {
      setIsLoading(false);
    }
  };

  const clearChat = () => {
    setMessages([
      {
        id: 1,
        role: 'assistant',
        content: `🤖 Bună! Sunt bibliotecarul tău AI. Îți pot recommanda cărți în funcție de interesele tale!

💡 **Exemple de întrebări:**
• 'Vreau o carte despre libertate și control social'
• 'Ce-mi recomanzi dacă iubesc poveștile fantastice?'
• 'Ce este 1984?'`,
        timestamp: new Date()
      }
    ]);
  };

  return (
    <div className="app">
      <header className="header">
        <div className="header-content">
          <h1>📚 Smart Librarian AI</h1>
          <p>Your AI-powered book recommendation assistant</p>
          <div className="header-actions">
            <button
              className="btn-secondary"
              onClick={() => setShowBooks(!showBooks)}
            >
              {showBooks ? 'Hide Books' : 'View Books'} ({books.length})
            </button>
            <button className="btn-secondary" onClick={clearChat}>
              🗑️ Clear Chat
            </button>
          </div>
        </div>
      </header>

      <div className="main-content">
        {showBooks && (
          <div className="books-sidebar">
            <h3>📖 Available Books</h3>
            <div className="books-list">
              {books.map((book) => (
                <div key={book.id} className="book-item">
                  <h4>{book.title}</h4>
                  <p>{book.summary}</p>
                </div>
              ))}
            </div>
          </div>
        )}

        <div className="chat-container">
          <div className="messages-container">
            {messages.map((message) => (
              <div key={message.id} className={`message ${message.role}`}>
                <div className="message-content">
                  <div className="message-text">
                    {message.content.split('\n').map((line, index) => (
                      <div key={index}>
                        {line}
                        {index < message.content.split('\n').length - 1 && <br />}
                      </div>
                    ))}
                  </div>
                  <div className="message-time">
                    {message.timestamp.toLocaleTimeString()}
                  </div>
                </div>
              </div>
            ))}
            {isLoading && (
              <div className="message assistant">
                <div className="message-content">
                  <div className="typing-indicator">
                    <span></span>
                    <span></span>
                    <span></span>
                  </div>
                </div>
              </div>
            )}
            <div ref={messagesEndRef} />
          </div>

          <form className="input-container" onSubmit={sendMessage}>
            <div className="input-wrapper">
              <input
                type="text"
                value={inputMessage}
                onChange={(e) => setInputMessage(e.target.value)}
                placeholder="Întreabă-mă despre cărți..."
                disabled={isLoading}
                className="message-input"
              />
              <button
                type="submit"
                disabled={isLoading || !inputMessage.trim()}
                className="send-button"
              >
                {isLoading ? '⏳' : '📤'}
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
}

export default App;