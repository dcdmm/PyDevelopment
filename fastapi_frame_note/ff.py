from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/get_data")
async def get_data(name: str, gender: str):
    # 直接使用函数的参数来获取GET请求的数据
    return JSONResponse(content={'name': name, 'gender': gender})

@app.post("/get_data")
async def post_data(request: Request):
    # FastAPI 使用 Pydantic 或 Request 对象来处理 POST 请求的数据
    if request.headers.get('Content-Type') == 'application/json':
        data = await request.json()
        return JSONResponse(content=data)
    else:
        form_data = await request.form()
        return JSONResponse(content=dict(form_data))
