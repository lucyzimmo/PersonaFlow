import React, { useState, useEffect } from "react";
import axios from "axios";

interface Message {
  user: string;
  ai: string;
}

interface Persona {
  name: string;
  system_prompt: string;
}

const Chat: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");
  const [persona, setPersona] = useState("research_assistant");
  const [personas, setPersonas] = useState<Record<string, Persona>>({});
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const fetchPersonas = async () => {
      try {
        const response = await axios.get("http://localhost:8000/personas");
        setPersonas(response.data);
      } catch (error) {
        console.error("Error fetching personas:", error);
      }
    };
    fetchPersonas();
  }, []);

  const sendMessage = async () => {
    if (!input.trim()) return;

    setLoading(true);
    try {
      const response = await axios.post("http://localhost:8000/chat", {
        user_id: "1234",
        persona,
        message: input,
      });

      setMessages((prev) => [
        ...prev,
        { user: input, ai: response.data.response },
      ]);
      setInput("");
    } catch (error) {
      console.error("Error sending message:", error);
      alert("Failed to send message. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="p-4 max-w-3xl mx-auto">
      <h1 className="text-3xl font-bold mb-4">PersonaFlow Chat</h1>

      <div className="mb-4">
        <label className="block text-sm font-medium mb-2">
          Select Persona:
        </label>
        <select
          className="w-full p-2 border rounded-lg"
          onChange={(e) => setPersona(e.target.value)}
          value={persona}
        >
          {Object.entries(personas).map(([key, value]) => (
            <option key={key} value={key}>
              {value.name}
            </option>
          ))}
        </select>
      </div>

      <div className="chat-box border rounded-lg p-4 h-[500px] overflow-y-auto mb-4 bg-gray-50">
        {messages.map((msg, i) => (
          <div key={i} className="mb-4">
            <div className="bg-blue-100 p-3 rounded-lg mb-2">
              <strong>User:</strong> {msg.user}
            </div>
            <div className="bg-white p-3 rounded-lg shadow">
              <strong>AI:</strong> {msg.ai}
            </div>
          </div>
        ))}
      </div>

      <div className="flex gap-2">
        <input
          className="flex-1 border rounded-lg p-2"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === "Enter" && sendMessage()}
          placeholder="Type your message..."
          disabled={loading}
        />
        <button
          className="bg-blue-500 text-white px-4 py-2 rounded-lg hover:bg-blue-600 disabled:bg-blue-300"
          onClick={sendMessage}
          disabled={loading}
        >
          {loading ? "Sending..." : "Send"}
        </button>
      </div>
    </div>
  );
};

export default Chat;
