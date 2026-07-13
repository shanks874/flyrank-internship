from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, this is my first API!"}

@app.get("/status")
def get_status():
    return {
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat()
    }