from typing import AsyncGenerator

from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import Depends

from database import get_async_session

from .models import User
from .schemas import UserReadSchema, UserCreateSchema

class UserRepository:
    def __init__(
        self,
        session: AsyncGenerator[AsyncSession, None] = Depends(get_async_session),
    ) -> None:
        self.session = session

    async def get_users(self) -> list[UserReadSchema]:
        ''' Get all users '''
        
        statement = select(User)
        result = await self.session.scalars(statement)

        return result 
        
    async def add_user(self, user: UserCreateSchema) -> bool:
        ''' Add new user '''

        # TODO make hashing password here
        statement = insert(
            User
        ).values(
            email=user.email,
            hashed_password=user.password
        )

        try:
            self.session.execute(statement)
        except:
            return False
        
        return True
        



