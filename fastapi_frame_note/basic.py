from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
# create a FastAPI "instance"
app = FastAPI()
class Item(BaseModel):
    name: str
    description: str = None
    price: float
    tax: float = None

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.api_route("/items/", methods=["GET", "POST"])
async def read_and_create_items(item: Item = None):
    if item:
        # 处理POST请求
        return {"message": "Item received", "item": item}
    else:
        # 处理GET请求
        return {"message": "This is a GET request, send a POST to see something different"}

if __name__ == '__main__':
    uvicorn.run(app, port=8000)
