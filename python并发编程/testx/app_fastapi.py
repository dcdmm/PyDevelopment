from fastapi import FastAPI

from main import get_time_io, get_time_cpu

app = FastAPI()


# uvicorn app_fastapi:app

@app.get("/duan")
async def hello_duan():
    a = get_time_cpu()
    return a


@app.get("/chao")
async def hello_chao():
    a = get_time_io()
    return a
