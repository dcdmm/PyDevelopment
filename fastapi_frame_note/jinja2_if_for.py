from fastapi import FastAPI
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/index")
def index(request: Request):
    age = 11
    lst = [1, 2, 3, 4, 5, 6]
    dit = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6}
    return templates.TemplateResponse(
        "jinja2_if_for.html",
        context={
            "request": request,  # context中必须添加该键值对
            "age": age,
            "lst": lst,
            "dit": dit
        }
    )


if __name__ == '__main__':
    uvicorn.run(app, port=8000)
