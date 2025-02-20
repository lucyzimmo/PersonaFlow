# Project: PersonaFlow - Adaptive AI Chatbot

## 📂 Folder Structure

```
PersonaFlow/
│── backend/                # FastAPI backend service
│   ├── main.py             # API endpoints & logic
│   ├── config.py           # Configurations (API keys, settings)
│   ├── memory.py           # FAISS-based memory storage
│   ├── personas.py         # Persona definitions & prompts
│   ├── embeddings.py       # Vector embeddings handler
│   ├── requirements.txt    # Backend dependencies
│── frontend/               # Next.js frontend application
│   ├── components/         # Reusable React components
│   ├── pages/              # Next.js pages
│   ├── styles/             # TailwindCSS styles
│   ├── api/                # API calls to backend
│   ├── package.json        # Frontend dependencies
│── README.md               # Project documentation
│── .env                    # API keys & environment variables
```

## 📝 README Template

# PersonaFlow - Adaptive AI Chatbot

** An intelligent, persona-driven chatbot powered by Mistral AI**

## 🚀 Features

- ** Multi-Persona AI**: Switch between different AI roles dynamically.
- ** Memory & Adaptation**: AI learns from user interactions.
- ** Hybrid Personas**: Merge multiple personas for cross-functional insights.
- ** Fast & Scalable**: Powered by FastAPI, Next.js, and FAISS memory retrieval.

## 🛠 Tech Stack

- ** Frontend**: Next.js (TypeScript), TailwindCSS
- ** Backend**: FastAPI (Python)
- ** LLM**: Mistral AI API
- ** Memory**: FAISS + PostgreSQL
- ** State Management**: Redis

## 📦 Setup Instructions

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-repo/personaflow.git
cd personaflow
```

### 2️⃣ Install Backend Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### 3️⃣ Install Frontend Dependencies

```bash
cd frontend
npm install
```

### 4️⃣ Run the Backend

```bash
uvicorn main:app --reload
```

### 5️⃣ Run the Frontend

```bash
npm run dev
```

## 📌 API Endpoints

| Method | Endpoint          | Description                    |
| ------ | ----------------- | ------------------------------ |
| `POST` | `/chat`           | Sends user message to AI       |
| `GET`  | `/personas`       | Lists available personas       |
| `POST` | `/set_persona`    | Switches to a specific persona |
| `POST` | `/merge_personas` | Combines multiple personas     |
| `GET`  | `/history`        | Retrieves past interactions    |

---
