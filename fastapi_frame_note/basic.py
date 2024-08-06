from fastapi import FastAPI, Request
import uvicorn

# create a FastAPI "instance"
app = FastAPI()


# 只接受`GET`请求
@app.get("/",
         tags=['GET'],
         summary="这是一个GET请求",
         description="GET请求,返回一个JSON字符串,内容为'Hello World'",
         response_description="Successful Response")
async def root():
    # 返回值类型可以为:字符串(singular values as str, int, etc.)、dict、list、Pydantic models
    return {"message": "Hello World, 你好,中国"}


# 只接受`POST`请求
@app.post("/get_data",
          # A list of tags to be applied to the path operation.
          # visible at /docs
          tags=['POST', 'get_data'],  # 默认为None
          # A summary for the path operation.
          # visible at /docs
          summary="这是一个POST请求",  # 默认为None
          # A description for the path operation.
          # If not provided, it will be extracted automatically from the docstring of the path operation function.
          # It can contain Markdown.
          # visible at /docs
          description="""POST请求,返回单个浮点数<p><font color='red' size=40>3.14159</font></p>
1. one
    * 1.1
        * 1.1.1
        * 1.1.2
    * 1.2
    * 1.3
2. tow
3. three """,  # 默认为None
          # The description for the default response.
          # visible at /docs
          response_description="Successful Response"  # 默认为None
          )
async def hello_world():
    return 3.14159


# 接受`GET`或`POST`请求
@app.get("/duan")
@app.post("/duan")
async def hello_python(request: Request):
    # HTTP请求方法
    request_method = request.method
    if request_method == 'GET':
        return "GET"
    if request.method == 'POST':
        return "POST"


if __name__ == '__main__':
    # API文档(浏览器打开):http://127.0.0.1:8000/docs
    uvicorn.run(app, port=8000)
