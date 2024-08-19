from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/items/")
# When you declare other function parameters that are not part of the path parameters, they are automatically interpreted as "query" parameters.
async def read_item(a: int, b: int = 10):  # 使用类型注解声明函数中查询参数的类型(a,b被声明为int类型);查询参数可以有默认值(b的默认值为10)
    # test: GET http://127.0.0.1:8000/items?a=0&b=10
    print(a)  # print->0
    print(b)  # print->10
    return a + b


@app.get("/users/{user_id}/items/{item_id}")
async def read_user_item(
        item_id: str,
        user_id: int,
        q: str | None = None,
        short: bool = False
):  # user_id、item_id为位置参数,q、short为查询参数;不需要按照特定顺序声明参数(参数通过名称识别)
    return {"user_id": user_id, "item_id": item_id, "q": q, "short": short}


if __name__ == '__main__':
    uvicorn.run(app, port=8000)
