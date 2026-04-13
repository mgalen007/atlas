# Atlas

A multi-agent research pipeline powered by Google Gemini. Given a topic, Atlas runs it through three specialized agents — a researcher, a critic, and a summarizer — and returns a clean, validated summary via a FastAPI gateway.

---

## How it works

```
Topic → [ Research Agent ] → [ Critic Agent ] → [ Summarizer Agent ] → Summary
```

1. **Research Agent** — gathers findings on the given topic
2. **Critic Agent** — validates the findings, filtering out anything unsupported
3. **Summarizer Agent** — produces a structured summary from the verified findings only

---

## Tech stack

- **Backend** — FastAPI
- **Agents** — [pydantic-ai](https://github.com/pydantic/pydantic-ai)
- **Model** — Google Gemini (via `google-generativeai`)
- **Validation** — Pydantic v2

---

## Prerequisites

- Python 3.11+
- A [Google Gemini API key](https://aistudio.google.com/app/apikey)

---

## Getting started

**1. Clone the repo**
```bash
git clone https://github.com/mgalen007/atlas.git
cd atlas
```

**2. Create and activate a virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up environment variables**
```bash
cp .env.example .env
```
Open `.env` and add your Gemini API key:
```
GEMINI_API_KEY=your_key_here
```

**5. Run the server**
```bash
cd server
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.

---

## API

### `GET /api/research?topic={topic}`

Runs the full research pipeline on a given topic.

**Example request**
```bash
curl "http://localhost:8000/api/research?topic=quantum+computing"
```

**Example response**
```json
{
  "success": true,
  "data": {
    "topic": "Quantum computing",
    "key_findings": [
      "Quantum computers use qubits instead of classical bits.",
      "Superposition allows qubits to represent multiple states simultaneously."
    ],
    "content": "Quantum computing represents a fundamental shift in how computation..."
  }
}
```
### `GET /api/health-check`

A health check endpoint, use it to verify if the server is running correctly.

### `GET /docs`

The Swagger UI documentation for the API.

---

## Project structure

```
atlas/
├── server/
│   ├── main.py
│   └── features/
│       ├── __init__.py
│       ├── research/
│       ├── __init__.py
│       │   └── router.py
│       └── agents/
│           ├── __init__.py 
│           ├── config/
│           │   └── models.py
│           ├── service.py
│           ├── research_agent.py
│           ├── critic_agent.py
│           └── summarizer_agent.py
├── client/               # frontend (coming soon)
├── .env.example
├── requirements.txt
└── README.md
```

---

## Screenshots

![screenshot](docs/screenshots/swagger.png)
Swagger UI docs

![screenshot](docs/screenshots/postman.png)
Example response in Postman for topic "Generative AI"

---

## License

MIT
