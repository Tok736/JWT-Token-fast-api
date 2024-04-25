from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker

from config import env_config

Base: DeclarativeMeta = declarative_base()

engine = create_async_engine(env_config.SQLALCHEMY_URL)
async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    ''' Function to get async database session '''
    async with async_session_maker() as session:
        yield session

