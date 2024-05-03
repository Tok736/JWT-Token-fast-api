from datetime import datetime

from pydantic import BaseModel


class UserReadSchema(BaseModel):
    id: int
    email: str

    registered_at: datetime
    updated_at: datetime


class UserCreateSchema(BaseModel):
    email: str
    password: str