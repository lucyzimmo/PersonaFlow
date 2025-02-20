# Project: PersonaFlow - Adaptive AI Chatbot

## Folder Structure

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
│   ├── pages/              # Next.js pages
│   ├── package.json        # Frontend dependencies
│── README.md               # Project documentation
│── .env                    # API keys & environment variables
```

## README Template

# PersonaFlow - Adaptive AI Chatbot

** An intelligent, persona-driven chatbot powered by Mistral AI **
Persona's include AI therapist, product manager, code reviewer, and research assistant.

## Features

- ** Multi-Persona AI**: Switch between different AI roles dynamically.
- ** Memory & Adaptation**: AI learns from user interactions.
- ** Fast & Scalable**: Powered by FastAPI, Next.js, and FAISS memory retrieval.

## Tech Stack

- ** Frontend**: Next.js (TypeScript), TailwindCSS
- ** Backend**: FastAPI (Python)
- ** LLM**: Mistral AI API
- ** Memory**: FAISS + PostgreSQL
- ** State Management**: Redis

## Setup Instructions

### Clone the Repository

```bash
git clone https://github.com/your-repo/personaflow.git
cd personaflow
```

### Install Backend Dependencies

```bash
cd backend
pip install -r requirements.txt
```

### Install Frontend Dependencies

```bash
cd frontend
npm install
```

### Run the Backend

```bash
uvicorn main:app --reload
```

### Run the Frontend

```bash
npm run dev
```

## 📌 API Endpoints

| Method | Endpoint       | Description                    |
| ------ | -------------- | ------------------------------ |
| `POST` | `/chat`        | Sends user message to AI       |
| `GET`  | `/personas`    | Lists available personas       |
| `POST` | `/set_persona` | Switches to a specific persona |
| `GET`  | `/history`     | Retrieves past interactions    |

---
