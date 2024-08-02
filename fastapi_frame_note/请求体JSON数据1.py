from typing import Annotated
import uvicorn
from fastapi import Body, FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float = Field(gt=0, description="The price must be greater than zero")
    tax: float | None = None


class User(BaseModel):
    username: str
    full_name: str | None = None


@app.post("/items0/{item_id}")
async def create_item0(
        item_id: int,
        importance: Annotated[int, Body()],  # 请求体JSON数据(单个值)参数(参数类型为Annotated[类型, Body()])
        q: str | None = None

):
    """
    test01:
    ```
    POST http://127.0.0.1:8000/items0/1/?q=china
    Content-Type: application/json

    3
    ```
    """
    print(item_id)  # test01 ===> print->1
    print(importance)  # test01 ===> print->3
    print(q)  # test0 ===> print->china
    return None


@app.post("/items10/")
async def create_item11(
        # 单个请求体JSON数据参数,想要参数名称作为请求体JSON数据中的键(参数类型为Annotated[类型, Body(embed=True))
        importance: Annotated[int, Body(embed=True)],
):
    """
    test01:

    POST http://127.0.0.1:8000/items10
    Content-Type: application/json

    {
      "importance": 3
    }
    """
    print(importance)  # test01 ===> print->3
    return None


@app.post("/items11/")
async def create_item11(
        # 单个请求体JSON数据参数,想要参数名称作为请求体JSON数据中的键(参数类型为Annotated[类型, Body(embed=True))
        item: Annotated[Item, Body(embed=True)]
):
    """
    test01:
    POST http://127.0.0.1:8000/items1
    Content-Type: application/json

    {
      "item": {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2
      }
    }
    """
    print(item)
    return None


@app.post("/items2/{item_id}")
async def create_item2(
        item_id: int,
        # 多个请求体JSON数据参数时,参数名称作为请求体JSON数据中的键
        item: Item, user: User, importance: Annotated[int, Body()],
        q: str | None = None
):
    """
    test01:
    POST http://127.0.0.1:8000/items2/1
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
      },
      "importance": 300
    }
    """
    print(item_id)  # test01 ===> print->1
    print(importance)  # test01 ===> print->300
    print(q)  # test01 ===> print->None
    print(item.model_dump())  # test01 ===> print->{'name': 'Foo', 'description': 'The pretender', 'price': 42.0, 'tax': 3.2}
    print(user.model_dump())  # test01 ===> print->{'username': 'dave', 'full_name': 'Dave Grohl'}
    return None


if __name__ == '__main__':
    uvicorn.run(app, port=8000)
