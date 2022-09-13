"""
API - application programming interface
"""
from fastapi import FastAPI


app = FastAPI()


@app.get("/")
def root():
    return {"message": "No message"}


@app.get("/ping")
def hello():
    return {"message": "pong"}
