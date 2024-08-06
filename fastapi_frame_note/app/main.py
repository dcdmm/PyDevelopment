from fastapi import FastAPI
import uvicorn

from sub import zero_sub
from sum import zero_plus
import mul

app = FastAPI()

# 添加该模块所有路由函数
app.include_router(zero_sub.router,
                   prefix='/xxx'  # 该模块所有所有路由函数路径添加前缀`/xxx`
                   )
app.include_router(zero_plus.router, prefix='/yyy')
app.include_router(mul.router)


@app.get("/")
async def root():
    return {"message": "Hello Bigger Applications!"}


if __name__ == '__main__':
    uvicorn.run(app, port=8000)
