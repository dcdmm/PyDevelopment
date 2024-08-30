from flask import Flask

from main import get_time_cpu, get_time_io

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
