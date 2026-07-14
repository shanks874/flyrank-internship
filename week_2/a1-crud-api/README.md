# Task API

A simple CRUD API built with FastAPI for the FlyRank Backend Internship Week 2 Assignment.

## Features

- Create tasks
- Read all tasks
- Read a single task
- Update tasks
- Delete tasks
- Swagger UI documentation

## Installation

Install dependencies:

```bash
pip install fastapi uvicorn
```

## Run the API

```bash
uvicorn main:app --reload
```

Server URL:

```text
http://localhost:8000
```

Swagger UI:

```text
http://localhost:8000/docs
```

## Endpoints

| Method | Endpoint | Description |
|----------|------------|-------------|
| GET | / | API information |
| GET | /health | Health check |
| GET | /tasks | Get all tasks |
| GET | /tasks/{task_id} | Get a task by ID |
| POST | /tasks | Create a task |
| PUT | /tasks/{task_id} | Update a task |
| DELETE | /tasks/{task_id} | Delete a task |

## Example curl Output

```bash
curl -i http://localhost:8000/tasks
```

Example response:

```json
[
  {
    "id": 1,
    "title": "Buy groceries",
    "done": false
  },
  {
    "id": 2,
    "title": "Finish assignment",
    "done": false
  },
  {
    "id": 3,
    "title": "Read a book",
    "done": true
  }
]
```

## Swagger UI

See the included Swagger screenshot/PDF demonstrating successful API testing.

## Author

Sasank