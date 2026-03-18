# AI FastAPI Assistant

Minimal backend project demonstrating how to integrate an AI-like assistant into a FastAPI application with persistent chat history using SQLite.

---

## Overview

This project is a **portfolio-ready backend service** designed to simulate an AI assistant system.

Key characteristics:

* Clean architecture (separation of concerns)
* FastAPI-based REST API
* SQLite for persistence
* Mocked AI responses (no external cost)
* Easily extensible to real AI APIs

---

## Features

* Single `/chat` endpoint
* Request/response schema validation
* Chat history storage in SQLite
* Mock AI response system (zero cost)
* Modular and scalable structure

---

## Project Structure

```
ai-fastapi-app/
│
├── app/
│   ├── main.py
│   ├── api/
│   │   └── routes.py
│   ├── core/
│   │   └── config.py
│   ├── services/
│   │   └── openai_service.py
│   ├── db/
│   │   ├── database.py
│   │   └── models.py
│   └── schemas/
│       └── chat.py
│
├── requirements.txt
├── .env
└── README.md
```

---

## Installation

### 1. Clone the repository

```bash
git clone <your-repo-url>
cd ai-fastapi-app
```

### 2. Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

```bash
uvicorn app.main:app --reload
```

Server will be available at:

```
http://127.0.0.1:8000
```

---

## API Documentation

Interactive Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## Endpoint

### POST `/chat`

#### Request

```json
{
  "message": "Hello"
}
```

#### Response

```json
{
  "response": "Hello. How can I assist you today?"
}
```

---

## Database

* SQLite database file: `chat.db`
* Table: `chat_history`

Stored fields:

* `id`
* `user_message`
* `ai_response`

---

## AI Mode (Mock vs Real)

The system uses a toggle inside:

```
app/services/openai_service.py
```

```python
USE_MOCK = True
```

### Mock Mode (default)

* No API cost
* Deterministic responses
* Ideal for demos and portfolios

### Real Mode

Set:

```python
USE_MOCK = False
```

Create a `.env` file:

```
OPENAI_API_KEY=your_key_here
```

---

## Limitations

* No conversation context (single message only)
* No user/session separation
* No streaming responses
* Basic error handling
* SQLite not suitable for high concurrency

---

## Suggested Improvements

* Add `conversation_id`
* Store full message history
* Inject context into responses
* Replace SQLite with PostgreSQL
* Add authentication layer
* Implement streaming responses
* Add logging and monitoring

---

## Purpose

This project is intended to:

* Demonstrate backend engineering skills
* Showcase API integration patterns
* Serve as a base for AI-enabled applications

---

## License

MIT License
