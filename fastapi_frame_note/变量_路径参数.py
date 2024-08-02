from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/items/{item_id}")
async def read_item(item_id):  # 路径参数`item_id`传递给函数参数`item_id`
    print(item_id, type(item_id))
    return {"item_id": item_id}  # test: `GET 127.0.0.1:8000/items/4` ===> print->4 <class 'str'>


@app.get("/items_typing/{item_id}")
async def read_item_typing(item_id: int):  # 使用类型注解声明函数中路径参数的类型(item_id被声明为int类型,默认为字符串)
    """
    # test01(HTTP error):
    `GET 127.0.0.1:8000/items_typing/chao`
    "msg": "Input should be a valid integer, unable to parse string as an integer"

    # test02(HTTP error):
    `GET 127.0.0.1:8000/items_typing/4.3`
    "msg": "Input should be a valid integer, unable to parse string as an integer",
    """
    print(item_id, type(item_id))  # test: `GET 127.0.0.1:8000/items_typing/4` ===> print->4 <class 'int'>
    return {"item_id": item_id}


if __name__ == '__main__':
    uvicorn.run(app, port=8000)
