from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


@app.get("/hello")
# takes a query parameter name
async def hello(name: str):
    return {"message": f"Hello {name}"}


@app.get("/health")
async def health():
    return {"time": datetime.now()}
