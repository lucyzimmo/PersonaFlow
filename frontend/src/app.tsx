import { useState } from "react";
import axios from "axios";
import React from "react";
import { marked } from "marked";
import hljs from "highlight.js";

// Define interfaces for props
interface PersonaSelectorProps {
  selectedPersona: string;
  onChange: (persona: string) => void;
}

// Persona Selector UI (React + Tailwind)
const PersonaSelector: React.FC<PersonaSelectorProps> = ({
  selectedPersona,
  onChange,
}) => {
  const personas = [
    "research_assistant",
    "code_reviewer",
    "product_manager",
    "ai_therapist",
  ];

  return (
    <div className="flex space-x-2">
      {personas.map((persona) => (
        <button
          key={persona}
          className={`px-4 py-2 rounded-md ${
            selectedPersona === persona
              ? "bg-blue-500 text-white"
              : "bg-gray-200"
          }`}
          onClick={() => onChange(persona)}
        >
          {persona.replace("_", " ")}
        </button>
      ))}
    </div>
  );
};

interface ChatInterfaceProps {
  userInput: string;
  setUserInput: (input: string) => void;
  onSend: () => void;
  messages: Array<{ role: string; content: string }>;
}

// Chat Interface (React + Tailwind)
const ChatInterface: React.FC<ChatInterfaceProps> = ({
  userInput,
  setUserInput,
  onSend,
  messages,
}) => {
  const highlightedContent = (content: string) => {
    const html = marked.parse(content, {
      breaks: true,
      gfm: true,
    });

    // Use highlight.js to highlight code blocks
    const tempDiv = document.createElement("div");
    tempDiv.innerHTML = html as string;

    const codeBlocks = tempDiv.querySelectorAll("pre code");
    codeBlocks.forEach((block) => {
      hljs.highlightElement(block as HTMLElement);
    });

    return tempDiv.innerHTML;
  };

  return (
    <div className="flex flex-col h-screen">
      <div className="flex-1 overflow-y-auto p-4 space-y-4">
        {messages.map((message, index) => (
          <div
            key={index}
            className={`mb-4 ${
              message.role === "user" ? "bg-blue-50" : "bg-white"
            } rounded-lg p-4 shadow`}
          >
            <div className="font-bold mb-2">
              {message.role === "user" ? "You:" : "AI:"}
            </div>
            <div
              className="prose max-w-none"
              dangerouslySetInnerHTML={{
                __html: highlightedContent(message.content),
              }}
            />
          </div>
        ))}
      </div>
      <div className="p-4">
        <input
          type="text"
          value={userInput}
          onChange={(e) => setUserInput(e.target.value)}
          placeholder="Type your message..."
          className="w-full p-2 border rounded-md"
        />
        <button
          onClick={onSend}
          className="mt-2 px-4 py-2 bg-blue-500 text-white rounded-md"
        >
          Send
        </button>
      </div>
    </div>
  );
};

// Main App Component (React + Tailwind)
const App: React.FC = () => {
  const [selectedPersona, setSelectedPersona] = useState("research_assistant");
  const [userInput, setUserInput] = useState("");
  const [messages, setMessages] = useState<
    Array<{ role: string; content: string }>
  >([]);

  const handleSend = async () => {
    if (userInput.trim()) {
      const newUserMessage = { role: "user", content: userInput };
      setMessages((prev) => [...prev, newUserMessage]);
      const currentInput = userInput;
      setUserInput("");

      try {
        console.log("Sending request to backend:", {
          user_id: "1234",
          persona: selectedPersona,
          message: currentInput,
        });

        const response = await axios.post(
          "http://localhost:8000/chat",
          {
            user_id: "1234",
            persona: selectedPersona,
            message: currentInput,
          },
          {
            headers: {
              "Content-Type": "application/json",
            },
          }
        );

        console.log("Received response:", response.data);

        if (response.data && response.data.response) {
          setMessages((prev) => [
            ...prev,
            { role: "ai", content: response.data.response },
          ]);
        } else {
          throw new Error("Invalid response format");
        }
      } catch (error) {
        console.error("Error sending message:", error);
        alert("Failed to send message. Please try again.");
      }
    }
  };

  return (
    <div className="flex flex-col h-screen p-4">
      <h1 className="text-2xl font-bold mb-4">PersonaFlow Chat</h1>
      <PersonaSelector
        selectedPersona={selectedPersona}
        onChange={setSelectedPersona}
      />
      <ChatInterface
        userInput={userInput}
        setUserInput={setUserInput}
        onSend={handleSend}
        messages={messages}
      />
    </div>
  );
};

export default App;
