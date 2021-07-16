import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
	name = os.getenv("USERNAME", "deta")
	return f"hello {name}!"