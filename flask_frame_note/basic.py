from flask import Flask
import logging

# flask程序报错时,会自动调用`logging.exceptio`方法记录错误信息
logging.basicConfig(filename='error.log', filemode='w', level=logging.NOTSET,
                    format="%(asctime)s %(name)s %(levelname)s %(message)s",
                    datefmt='%Y-%m-%d  %H:%M:%S %a')

# 实例化
app = Flask(__name__)


# 接受'GET'与'POST'请求
@app.route("/duan", methods=['GET', 'POST'])
def hello_world():
    return "<p>Hello, World!</p>"  # 返回值类型可以为:字符串、JSON数据、Renders a template


# 只接受'GET'请求
@app.route("/chao", methods=['GET'])
def hello_python():
    # 不设置debug=True ===> 浏览器中提示Internal Server Error,看不到错误的详细信息
    # 设置debug=True ===> 浏览器中显示错误类型ZeroDivisionError,并给出错误的详细信息
    a = 1 / 0
    return "<p>Hello, Python!</p>"


'''
:param host: the hostname to listen on. Set this to ``'0.0.0.0'`` to
    have the server available externally as well. Defaults to
    ``'127.0.0.1'`` or the host in the ``SERVER_NAME`` config variable
    if present
    
:param port: the port of the webserver. Defaults to ``5000`` or the
    port defined in the ``SERVER_NAME`` config variable if present.
'''
if __name__ == '__main__':
    # app.run(host='0.0.0.0') # 还可以通过`curl http://外网ip地址:5000/duan`访问
    app.run(port=5001)
    # app.run(debug=True, port=5001)  # test:`curl http://127.0.0.1:5001/duan`或`curl http://内网ip地址:5001/duan`
