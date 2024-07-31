from fastapi import FastAPI
import uvicorn

# create a FastAPI "instance"
app = FastAPI()


# 只接受'GET'请求
@app.get("/")
async def root():
    # 返回值类型可以为:字符串、JSON数据、Pydantic models
    return {"message": "Hello World"}


if __name__ == '__main__':
    uvicorn.run(app, port=8000)
