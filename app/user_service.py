import httpx
from sqlalchemy import DateTime
from datetime import datetime, timezone, timedelta
from app.user_schemas import UserSchema, UserResponseSchema


CAT_FACTS_URL = "https://catfact.ninja/fact"


async def get_facts() -> str:
    """"Fetches facts from CAT_FACTS_URL and returns them as a string"""
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(CAT_FACTS_URL)
            response.raise_for_status()
            data = response.json()
            return data.get("fact")
    except Exception:
        return "An error occurred while loading facts: {}"


async def get_user() -> UserResponseSchema:
    """This function combine static user information and fetches catfacts API"""
    fact = await get_facts()
    users = UserSchema(
        email="estheranierobi146@gmail.com",
        name="Esther Anierobi",
        stack="Python/FastAPI"
    )

    return UserResponseSchema(
        status="success",
        user=users,
        timestamp=datetime.now(timezone.utc).isoformat(),
        fact=fact
    )
