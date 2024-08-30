from flask import Flask

from main import get_time

app = Flask(__name__)


@app.route("/duan", methods=['GET', 'POST'])
def hello_world():
    a = get_time()
    return str(a)