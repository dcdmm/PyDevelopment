from fastapi import Request, FastAPI
import uvicorn

app = FastAPI()


@app.post("/post_data/{item_id}")
async def post_data(request: Request):
    """
    # test01
    ```
    POST http://127.0.0.1:8000/post_data/1?a=1&b=2
    Content-Type: application/json
    name: dcdmm
    age: 100
    love: play_computer_game

    {
      "name": "dcdmm",
      "age": 1000
    }
    ```
    """
    """
    # test02
    ```
    POST http://127.0.0.1:8000/post_data
    Content-Type: application/x-www-form-urlencoded
    
    data=123
    ```
    """
    print(request.path_params.items())  # test01 ===> print->dict_items([('item_id', '1')])
    # test01 ===> print->dict_items([('a', '1'), ('b', '2')])
    # test02 ===> print->dict_items([])
    print(request.query_params.items())
    header = request.headers
    print(header.get('name'))  # test01 ===> print->dcdmm
    print(header.get('age'))  # test01 ===> print->100
    print(header.get('love'))  # test01 ===> print->play_computer_game
    print(header.get('Content-Type'))  # test01 ===> print->application/json

    # test01 ===> print->http://127.0.0.1:8000/get_data
    # test02 ===> print->application/x-www-form-urlencoded
    print(request.url)
    if request.headers.get('Content-Type') == 'application/json':
        data = await request.json()  # json是协程函数(前添加`await`关键字)
        print(data)  # test01 ===> print->{'name': 'dcdmm', 'age': 1000}
    else:
        form_data = await request.form() # form是协程函数(前添加`await`关键字)
        print(form_data)  # test02 ===> print->FormData([('data', '123')])
        print(type(form_data))  # test02 ===> print-><class 'starlette.datastructures.FormData'>
        print(form_data.get("data"))  # test02 ===> print->123
    return None


if __name__ == '__main__':
    uvicorn.run(app, port=8000)
