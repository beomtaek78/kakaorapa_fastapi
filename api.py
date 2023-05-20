from fastapi import FastAPI
from beomtaek import beomtaek_router

app = FastAPI()

@app.get("/")
async def welcome() -> dict:
    return {
            "message": "Hello World"
    }

app.include_router(beomtaek_router)
