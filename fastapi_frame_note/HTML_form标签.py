from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/index0")
async def index0(request: Request):
    query = dict(request.query_params.items())
    print(query.get('name_'))
    print(query.get('password_'))
    return templates.TemplateResponse("form_get.html", {"request": request})


# @app.get("/index1")
# @app.post("/index1")
# async def index1(request: Request):
#     return templates.TemplateResponse("form_post.html", {"request": request})


if __name__ == "__main__":
    uvicorn.run(app)
