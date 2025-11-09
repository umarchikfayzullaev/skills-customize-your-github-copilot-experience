```markdown
# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a small REST API using the FastAPI framework. You will create endpoints, use Pydantic models for validation, and run an async web server.

## 🧭 Prerequisites

- Basic Python (functions, typing)
- Familiarity with HTTP verbs (GET, POST)

## 🔍 Skills practiced

- Designing REST endpoints
- Request validation with Pydantic
- Asynchronous request handling
- Running and testing an API locally

## 📅 Due date

- 2025-11-16 (auto-generated)

## 📝 Tasks

### 🛠️ Task 1 — Core: Build a simple API

#### Description
Create a FastAPI application that provides CRUD-like endpoints for a small resource (for example, "items"). Implement at least a GET (list), GET (single), and POST endpoint.

#### Requirements (must-haves)

The finished project must:

- Provide a minimal FastAPI app (`starter-code.py`) that can be run with Uvicorn.
- Expose a GET endpoint that lists items and a GET endpoint that returns a single item by ID.
- Expose a POST endpoint that accepts a Pydantic model, validates input, and returns the created resource.
- Use Pydantic models for request/response validation and include clear example payloads in the docs.
- Include concise instructions for installing dependencies and running the server.

### 🛠️ Task 2 — Optional/Bonus

- Add PUT/PATCH and DELETE endpoints.
- Persist data to a simple JSON file for session persistence.
- Add basic tests (pytest) for the API endpoints.

## 📁 Starter files

- `starter-code.py` — minimal FastAPI app (included).
- `requirements.txt` — required packages.

Run the app locally:

```bash
pip install -r assignments/fastapi-rest-apis/requirements.txt
uvicorn assignments.fastapi-rest-apis.starter-code:app --reload --port 8000
```

or from the assignment folder:

```bash
cd assignments/fastapi-rest-apis
pip install -r requirements.txt
uvicorn starter-code:app --reload --port 8000
```

After the server starts, open the interactive docs at: `http://127.0.0.1:8000/docs`

## ✅ Submission & Grading checklist

- App runs without syntax errors using Python 3.8+.
- GET and POST endpoints work and validate input.
- README includes run instructions and a brief description of endpoints.
- Bonus features (if present) are documented.

## 💡 Hints and Edge Cases

- Use `typing.Optional` for optional fields and default values.
- Validate JSON payload shapes with Pydantic models.
- Test the API in the browser via `/docs` or with `curl`/HTTPie.

---

If you'd like, I can also add simple tests (`pytest`) or a small JSON-backed persistence example.

```
