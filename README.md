# Adaptive Diagnostic Engine

A GRE-style adaptive testing system that adjusts question difficulty in real time based on how the student is performing. Built with FastAPI, MongoDB, and OpenAI.

## What it does

Instead of giving everyone the same questions, this system tracks how well you're doing and picks the next question accordingly. Get one right and the next one gets harder. Get one wrong and it backs off. After 10 questions it uses GPT to generate a study plan based on where you struggled.

## Tech Stack
- **Backend:** Python + FastAPI
- **Database:** MongoDB Atlas
- **AI:** OpenAI GPT-3.5-turbo

## Setup

### 1. Clone the repo
```bash
git clone https://github.com/yourusername/adaptive-engine.git
cd adaptive-engine
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Create a `.env` file in the root
```
MONGODB_URI=your_mongodb_uri_here
OPENAI_API_KEY=your_openai_key_here
```

### 4. Seed the database
```bash
python seed.py
```

### 5. Start the server
```bash
uvicorn main:app --reload
```

### 6. Test the API
Go to `http://127.0.0.1:8000/docs` — Swagger UI lets you test everything interactively.

---

## How the Adaptive Algorithm Works

I used the **1PL IRT (Item Response Theory)** model as the backbone.

The core idea is simple: every student has an "ability score" and every question has a "difficulty score". The probability of a student getting a question right is:
```
P(correct) = 1 / (1 + e^-(ability - difficulty))
```

After each answer, I update the ability score:
- **Correct answer:** ability goes up, but less so if the question was easy (you're supposed to get easy ones right)
- **Wrong answer:** ability goes down, but less so if the question was hard (missing a hard one isn't a big deal)

The next question is always the one whose difficulty is closest to the student's current ability. This keeps the test in the "zone of proximal development" — not too easy, not too hard.

Ability is capped between 0.1 and 1.0 to match the question difficulty range.

---

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Check if server is running |
| POST | `/session/start` | Start a new test, returns first question |
| POST | `/session/answer` | Submit answer, get next question |
| GET | `/session/report/{session_id}` | Get personalized AI study plan |

---

## AI Log

I used Claude and ChatGPT throughout this project, mainly to move faster on boilerplate stuff like setting up FastAPI routes and Pydantic models. The IRT math I worked through myself first on paper, then used AI to help translate it into clean Python.

A few things AI couldn't help with directly:
- The MongoDB Atlas SSL error was a rabbit hole — AI kept suggesting the same fixes that weren't working. Eventually figured out it needed `certifi` for proper TLS certificate handling on Windows.
- Getting the virtual environment working on PowerShell was a manual fix (execution policy issue on Windows).

Overall I'd say AI saved me a few hours on setup and syntax, but the architectural decisions and debugging were mostly hands-on.