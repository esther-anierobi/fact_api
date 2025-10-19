from fastapi import APIRouter
from starlette import status
from app.user_service import get_user
from app.user_schemas import UserResponseSchema


router = APIRouter(prefix="/me", tags=[""])




@router.get("/", response_model=UserResponseSchema, status_code=status.HTTP_200_OK)
async def me():
    return await get_user()

