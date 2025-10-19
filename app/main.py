from fastapi import FastAPI
from app import user_route

app = FastAPI(title="My Profile")


@app.get("/", operation_id="Profile")
async def root():
    return {"message": "Welcome to fastAPI and Cat URL"}


app.include_router(user_route.router)
