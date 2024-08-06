from fastapi import FastAPI
import uvicorn
from fastapi.templating import Jinja2Templates
from fastapi import Request

app = FastAPI()

templates = Jinja2Templates(directory="templates")


class Play:
    play_min = 34

    def play_info(self, describe):
        return "玩的" + describe + "开心"


@app.get("/index")
def index(request: Request):
    name = "dcdmm"
    age = 3
    like = ['football', 'game', 'music']
    other = {"countery": "china", "grade": "A"}
    p = Play()

    return templates.TemplateResponse(
        "jinja2_variables.html",
        context={
            "request": request,  # context中必须添加该键值对
            "user_name": name,
            "user_age": age,
            "user_like": like,
            "user_other": other,
            "user_play": p
        }
    )


if __name__ == '__main__':
    uvicorn.run(app, port=8000)
