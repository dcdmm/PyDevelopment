from fastapi import FastAPI
import uvicorn

# create a FastAPI "instance"
app = FastAPI()


# 只接受'GET'请求
@app.get("/")
async def root():
    a = 1 / 0
    return "<p>Hello, Python!</p>"


if __name__ == '__main__':
    uvicorn.run(app, port=8000)
