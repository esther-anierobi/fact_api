import datetime
import uuid
from uuid import UUID

from sqlalchemy import Column, String, DateTime
from app.database import Base


class User(Base):
    __tablename__ = 'users'

    email = Column(String, unique=True, primary_key=True, index=True)
    name = Column(String, nullable=False)
    user_stack = Column(String, nullable=False)
    # created_at = Column(DateTime(timezone=True), nullable=False, server_default=str(datetime.UTC.utc))

