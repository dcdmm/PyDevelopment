from fastapi import APIRouter

router = APIRouter()


@router.get("/sub/", tags=["sub"])
async def read_users():
    return 0


@router.get("/sub/1", tags=["sub"])
async def read_user_me():
    return -1


@router.get("/sub/{num}", tags=["sub"])
async def read_user(num: int):
    return 1 - num
