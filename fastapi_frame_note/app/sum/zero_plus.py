from fastapi import APIRouter

# You can think of APIRouter as a "mini FastAPI" class. All the same options are supported.
router = APIRouter()


@router.get("/sum/", tags=["sum"])
async def read_users():
    return 0


@router.get("/sum/1", tags=["sum"])
async def read_user_me():
    return 1


@router.get("/sum/{num}", tags=["sum"])
async def read_user(num: int):
    return 1 + num
