from flask import Flask

app = Flask(__name__)


# string: 字符串(不包括斜杠符(/));默认
# int: 整数
# float: 浮点值
# path: 接受用作目录分隔符的斜杠符(/)
@app.route('/user/<int:num>')  # num表示变量
def index(num):
    if num == 1:
        # test:curl http://127.0.0.1:5000/user/1
        return "1: python"
    if num == 2:
        # test:curl http://127.0.0.1:5000/user/2
        return "2: java"
    if num == 3:
        # test:curl http://127.0.0.1:5000/user/3
        return "3: c++"
    return "other: hello world"


if __name__ == '__main__':
    app.run()
