from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/users", tags=["users"], summary="Get all users")
async def get_users():
    return {"id": 1, "username": "Who?", "email": "who@email.com"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0")