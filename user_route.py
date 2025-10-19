from fastapi import APIRouter
from starlette import status
from user_service import get_user
from user_schemas import UserResponseSchema


router = APIRouter(prefix="/me")


@router.get("/", operation_id="me", tags=["Profile"], response_model=UserResponseSchema, status_code=status.HTTP_200_OK)
async def get_all():
    return await get_user()

