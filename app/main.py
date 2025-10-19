from fastapi import FastAPI
from app import user_route

app = FastAPI(title="My Profile")


app.include_router(
    user_route.router
)
