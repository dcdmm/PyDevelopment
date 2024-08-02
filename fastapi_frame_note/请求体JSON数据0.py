from fastapi import FastAPI
from pydantic import BaseModel, Field
import uvicorn


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None


app = FastAPI()


@app.post("/items/{item_id}")
async def create_item(
        item_id: int,  # 路径参数
        item: Item | None = None,  # 请求体JSON数据(dict)参数(参数类型继承自pydantic BaseModel)
        q: str | None = None  # 查询参数
):
    """
    # test01
    ```
    POST http://127.0.0.1:8000/items/1?q=china
    Content-Type: application/json
    ```
    """
    """
    # test02
    ```
    POST http://127.0.0.1:8000/items/1?q=china
    Content-Type: application/json
    
    {
        "name": "Foo",
        "description": "An optional description",
        "price": 45.2,
        "tax": 3.5
    }
    ```
    """
    print(item_id)
    print(q)
    if item is not None:
        item_dict = item.model_dump()
        print(item_dict)
    else:
        # test01 ===> print->None
        # test02 ===> {'name': 'Foo', 'description': 'An optional description', 'price': 45.2, 'tax': 3.5}
        print("None")
    return item


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.post("/items_many/{item_id}")
async def update_item(
        item_id: int,
        # 多个请求体JSON数据参数时,参数名称作为请求体JSON数据中的键
        item: Item, user: User
):
    """
    test:
    ```
    POST http://127.0.0.1:8000/items_many/1
    Content-Type: application/json

    {
      "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
      },
      "user": {
        "username": "dave",
        "full_name": "Dave Grohl"
      }
    }
    ```
    """
    results = {"item_id": item_id, "item": item, "user": user}
    print(item.model_dump())  # test01 ===> {'name': 'Foo', 'description': 'The pretender', 'price': 42.0, 'tax': 3.2}
    print(user.model_dump())  # test02 ===> {'username': 'dave', 'full_name': 'Dave Grohl'}
    return results


if __name__ == '__main__':
    uvicorn.run(app, port=8000)
