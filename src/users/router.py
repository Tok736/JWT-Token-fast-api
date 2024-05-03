from fastapi import APIRouter, Depends

from .repository import UserRepository
from .schemas import UserCreateSchema, UserReadSchema

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

@router.get("/")
async def get_users(
    repository: UserRepository = Depends()
) -> list[UserReadSchema]:
    ''' Эндпоинт для получения всех пользователей '''
    return await repository.get_users()

@router.post("/")
async def add_user(
    user: UserCreateSchema,
    repository: UserRepository = Depends()
) -> list[UserReadSchema]:
    ''' Эндпоинт для добавления нового пользователя '''
    return await repository.add_user(user)


