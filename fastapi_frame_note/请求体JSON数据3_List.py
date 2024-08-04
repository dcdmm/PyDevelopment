from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel

app = FastAPI()


@app.post("/items/")
async def create_item0(items: list[int]):  # 请求体JSON数据(list)参数(参数类型为list[类型])
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
async def create_item0(items: list[Item]):
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


@app.post("/index-weights/")
async def create_index_weights(weights: dict[int, float]):
    """
    # test
    ```
    POST 127.0.0.1:8000/index-weights
    Content-Type: application/json

    {
      "1": 2.4,
      "2": 4.34
    }
    ```
    """
    print(weights)  # print->{1: 2.4, 2: 4.34}
    return None


if __name__ == "__main__":
    uvicorn.run(app)
