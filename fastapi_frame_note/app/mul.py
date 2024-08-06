from fastapi import APIRouter

router = APIRouter()


@router.get("/mul/", tags=["mul"])
async def read_users():
    return 1


@router.get("/mul/1", tags=["mul"])
async def read_user_me():
    return 1


@router.get("/mul/{num}", tags=["mul"])
async def read_user(num: int):
    return 1 * num
