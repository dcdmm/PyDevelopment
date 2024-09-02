from flask import Flask
import asyncio

from main import get_time_cpu, get_time_io, complex
from utily import async_computer

app = Flask(__name__)

# flask --app app_flask:app run


@app.route("/duan", methods=['GET', 'POST'])
def hello_duan():
    a = get_time_cpu()
    return str(a)


@app.route("/chao", methods=['GET', 'POST'])
def hello_chao():
    a = get_time_io()
    return str(a)


@app.route("/dmm", methods=['GET', 'POST'])
def hello_dmm():
    # 单线程模式多个请求时,每个请求需要等待前一个请求完全处理完毕(尽管async_computer内部是异步执行的)
    use_time = asyncio.run(async_computer())
    return str(use_time)


@app.route("/dcdmm", methods=['GET', 'POST'])
def hello_dcdmm():
    use_time = asyncio.run(complex())
    return str(use_time)
