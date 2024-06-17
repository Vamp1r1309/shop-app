from fastapi import APIRouter

from .schemas import CreateUser
from .crud import create_in_user

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
async def create_user(user: CreateUser):
    return create_in_user(user_in=user)