from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


app = FastAPI()


@app.post("/items/{item_id}")
async def create_item(
        item_id: int,  # 路径参数
        item: Item,  # 请求体JSON数据(类型继承自pydantic BaseModel)
        q: str | None = None  # 查询参数
):
    print(item_id)
    print(q)
    item_dict = item.model_dump()
    print(item_dict)
    return item


if __name__ == '__main__':
    uvicorn.run(app, port=8000)
