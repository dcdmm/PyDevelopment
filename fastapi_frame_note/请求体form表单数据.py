from typing import Annotated
import uvicorn
from fastapi import FastAPI, Form

app = FastAPI()


@app.post("/login/")
async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
    """
    test01:
    POST http://127.0.0.1:8000/login/
    Content-Type: application/x-www-form-urlencoded

    username=dcdmm&password=123456
    """
    print(username)  # test01 ===> print->dcdmm
    print(password)  # test01 ===> print->123456
    return None


if __name__ == '__main__':
    uvicorn.run(app, port=8000)
