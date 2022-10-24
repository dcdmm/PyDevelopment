from flask import Flask

# 实例化
app = Flask(__name__)


# http://127.0.0.1:5000/duan
# 接受'GET'与'POST'请求
@app.route("/duan", methods=['GET', 'POST'])
def hello_world():
    return "<p>Hello, World!</p>"


# curl http://127.0.0.1:5000/chao    ===>    host='0.0.0.0' or host='127.0.0.1'
# curl http://内网ip:5000/duan    ===>    host='0.0.0.0'
# 只接受'POST'请求
@app.route("/chao", methods=['POST'])
def hello_python():
    return "<p>Hello, Python!</p>"

'''
:param host: the hostname to listen on. Set this to ``'0.0.0.0'`` to
    have the server available externally as well. Defaults to
    ``'127.0.0.1'`` or the host in the ``SERVER_NAME`` config variable
    if present
'''
if __name__ == '__main__':
    # app.run(host='0.0.0.0')  #
    app.run()