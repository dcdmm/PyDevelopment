from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()


class Image(BaseModel):
    url: str
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    images: list[Image] | None = None  # Nested Models(类型为其他的Pydantic model)


@app.post("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    """
    test:
    POST http://127.0.0.1:8000/items/1
    Content-Type: application/json

    {
        "name": "Foo",
        "description": "The pretender",
        "price": 42.0,
        "tax": 3.2,
        "tags": [
            "rock",
            "metal",
            "bar"
        ],
        "images": [
            {
                "url": "http://example.com/baz.jpg",
                "name": "The Foo live"
            },
            {
                "url": "http://example.com/dave.jpg",
                "name": "The Baz"
            }
        ]
    }
    """
    results = {"item_id": item_id, "item": item}
    return results


if __name__ == '__main__':
    uvicorn.run(app, port=8000)
