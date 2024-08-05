from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()


@app.post("/items/")
async def create_item0(items: list[int]):  # 请求体JSON数据(list)参数(参数类型为list[类型],这里类型为int)
    """
    # test:
    ```
    POST 127.0.0.1:8000/items
    Content-Type: application/json

    [1, 2, 3]
    ```
    """
    print(items)  # print->[1, 2, 3]
    return None


class Item(BaseModel):
    name: str
    description: str | None = None


@app.post("/items_p/")
async def create_item0(items: list[Item]):  # 请求体JSON数据(list)参数(参数类型为list[类型],这里类型为Item)
    """
    # test:
    ```
    POST 127.0.0.1:8000/items_p
    Content-Type: application/json

    [
      {
        "name": "dcdmm",
        "description": "good"
      },
       {
        "name": "dc",
        "description": "verge good"
      }
    ]
    ```
    """
    print(items)  # print->[Item(name='dcdmm', description='good'), Item(name='dc', description='verge good')]
    return None


@app.post("/items_d/")
async def create_item1(items: list[dict[str, str]]):  # 请求体JSON数据(list)参数(参数类型为list[类型],这里类型为dict[str, str])
    """
    # test:
    ```
    POST 127.0.0.1:8000/items_d
    Content-Type: application/json

    [
      {
        "name": "dcdmm",
        "description": "good"
      },
       {
        "name": "dc",
        "description": "verge good"
      }
    ]
    ```
    """
    print(items)  # print->[{'name': 'dcdmm', 'description': 'good'}, {'name': 'dc', 'description': 'verge good'}]
    return None


@app.post("/index-weights/")
async def create_index_weights(weights: dict[int, float]):  # 请求体JSON数据(dict)参数(参数类型为list[类型1, 类型2],这里类型1为int,类型2为float)
    """
    # test
    ```
    POST 127.0.0.1:8000/index-weights
    Content-Type: application/json

    # Keep in mind that JSON only supports str as keys.
    {
      "1": 2.4,
      "2": 4.34
    }
    ```
    """
    print(weights)  # print->{1: 2.4, 2: 4.34}
    print(type(list(weights.keys())[0]))  # print->int
    print(type(list(weights.values())[0]))  # print->float
    return None


if __name__ == "__main__":
    uvicorn.run(app)
