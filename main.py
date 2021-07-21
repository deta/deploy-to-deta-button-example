import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def index():
	name = os.getenv("USERNAME", "world")
	return f"hello {name}!"