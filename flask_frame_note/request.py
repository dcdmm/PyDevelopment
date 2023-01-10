from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/get_data', methods=['GET', 'POST'])
def example_get():
    if request.method == 'GET':
        # test:curl "http://127.0.0.1:5000/get_data?name=frank&gender=male"
        print(request.args)  # 获取url中的参数
        print(type(request.args))  # werkzeug.datastructures.ImmutableMultiDict
        name = request.args.get('name')
        gender = request.args.get('gender')
        return jsonify({'name': name, 'gender': gender})

    if request.method == 'POST':
        # test:curl -H "Content-Type: application/json" http://127.0.0.1:5000/get_data -d '{"data":123}' -X POST
        data_json = request.json
        if data_json is not None:
            print(data_json)  # {'data': 123}
            print(type(data_json))  # dict
            return jsonify(data_json)  # {"data":123}
        else:
            # test:curl http://127.0.0.1:5000/get_data -d 'data=123' -X POST
            print(request.form)  # ImmutableMultiDict([('data', '123')])
            print(type(request.form))  # werkzeug.datastructures.ImmutableMultiDict
            print(request.form.get('data'))  # 123
            return jsonify(request.form)  # {"data":"123"}


if __name__ == '__main__':
    app.run()
