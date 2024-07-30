from flask import Flask, render_template, request
from flask import jsonify

app = Flask(__name__)


@app.route('/index0', methods=['GET'])
def index0():
    """
    分析:
    1. 浏览器访问http://127.0.0.1:5000/index0
        1. 打印None, None
        2. 渲染example_get.html内容
    2. 单行文本输入框输入11,密码输入框输入22(发送表单数据时所用的HTTP方法为get)
        1. print语句打印11, 22
        2. 渲染example_get.html内容
    ......
    """
    # request.method:The method the request was made with, such as GET.
    if request.method == 'GET':
        name = request.args.get('name_')
        password = request.args.get('password_')
        print(name, password)
        # Renders a template from the template folder with the given context.
        return render_template('example_get.html')


@app.route('/index1', methods=['GET', 'POST'])
def index1():
    """
    分析:
    1. 浏览器访问http://127.0.0.1:5000/index1
        1. 渲染example_get.html内容
    2. 单行文本输入框输入11,密码输入框输入22(发送表单数据时所用的HTTP方法为post)
        1. print语句打印11, 22
        2. 返回JSON数据{"name":"11","password":"22"}
    """
    if request.method == 'POST':
        name = request.form.get('name_')  # 从form表单获取name_属性
        password = request.form.get('password_')  # 从form表单获取password_属性
        print(name, password)
        return jsonify({'name': name, 'password': password})
    return render_template('example_post.html')


if __name__ == '__main__':
    app.run()
