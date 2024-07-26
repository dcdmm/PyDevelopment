from fastapi import FastAPI
from fastapi.templating import Jinja2Templates
app = FastAPI()


@app.get("/a")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}

import uvicorn

if __name__ == '__main__':

    uvicorn.run(app,  port=8000)