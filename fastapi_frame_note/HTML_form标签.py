from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/index0")
async def index0(request: Request):
    """参考PyDevelopment\flask_frame_note\HTML_form标签.py"""
    query = dict(request.query_params.items())
    print(query.get('name_'))
    print(query.get('password_'))
    return templates.TemplateResponse("form_get.html", {"request": request})


@app.get("/index1")
@app.post("/index1")
async def index1(request: Request):
    """参考PyDevelopment\flask_frame_note\HTML_form标签.py"""
    if request.method == 'POST':
        form_data = await request.form()
        name = form_data.get('name_')  # 从form表单获取name_属性
        password = form_data.get('password_')  # 从form表单获取password_属性
        print(name, password)
        return {'name': name, 'password': password}
    return templates.TemplateResponse("form_post.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run(app)
