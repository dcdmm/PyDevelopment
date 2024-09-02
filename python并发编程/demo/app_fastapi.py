from fastapi import FastAPI

from main import get_time_io, get_time_cpu, complex
from utily import async_computer

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


@app.get("/dmm")
async def hello_dmm():
    # 单线程模式多个请求时,对于I/O密集型任务,无需等待前一个请求完全处理完毕(异步)
    use_time = await async_computer()
    return use_time


@app.get("/dcdmm")
async def hello_dmm():
    use_time = await complex()
    return use_time
