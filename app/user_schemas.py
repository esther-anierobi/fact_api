from datetime import datetime, timezone
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    email: str
    name: str
    stack: str


class UserResponseSchema(BaseModel):
    status: str
    user: UserSchema
    timestamp: datetime
    fact: str

    # class Config:
    #     orm_mode = True
