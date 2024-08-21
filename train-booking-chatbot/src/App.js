import React, { useState } from 'react';
import './App.css';

function App() {
  const [messages, setMessages] = useState([
    { text: 'Welcome! How can I assist you today?', sender: 'bot' },
  ]);
  const [inputValue, setInputValue] = useState('');
  const [sessionId, setSessionId] = useState('');

  const handleSendMessage = async () => {
    if (inputValue.trim()) {
      const newMessages = [...messages, { text: inputValue, sender: 'user' }];
      setMessages(newMessages);

      try {
        const response = await fetch('http://localhost:5000/api/chatbot', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ message: inputValue, session_id: sessionId }),
        });
        const data = await response.json();
        setMessages([...newMessages, { text: data.reply, sender: 'bot' }]);
        if (!sessionId && data.session_id) setSessionId(data.session_id);  // Set session ID if not present
      } catch (error) {
        setMessages([...newMessages, { text: 'Sorry, something went wrong!', sender: 'bot' }]);
      }
    }
    setInputValue('');
  };

  return (
    <div className="App">
      <h1>Train Ticket Booking System</h1>
      <div className="chat-window">
        <div className="messages">
          {messages.map((message, index) => (
            <div key={index} className={`message ${message.sender}`}>
              {message.text}
            </div>
          ))}
        </div>
        <div className="input-area">
          <input
            type="text"
            value={inputValue}
            onChange={(e) => setInputValue(e.target.value)}
            onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
          />
          <button onClick={handleSendMessage}>Send</button>
        </div>
      </div>
    </div>
  );
}

export default App;
