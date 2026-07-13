# BE-01: First API Endpoint

A minimal FastAPI backend with two JSON endpoints.

## Setup
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Run
```bash
uvicorn main:app --reload
```

## Endpoints
- `GET /` — welcome message
- `GET /status` — status + current UTC timestamp

## Test
```bash
curl http://127.0.0.1:8000
curl http://127.0.0.1:8000/status
```