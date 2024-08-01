from flask import Flask, jsonify

app = Flask(__name__)
# Serialize objects to ASCII-encoded JSON. If this is disabled, the JSON returned from jsonify will contain Unicode characters.
app.json.ensure_ascii = False  # 通过设置app.json.ensure_ascii = False,使其正常显示中文


@app.route('/index')
def index():
    data = {
        'name': '您本次体检血压示:<b>150182 mmHg</b>。'
    }

    # Serialize the given arguments as JSON, and return a :class:`~flask.Response` object with the ``application/json`` mimetype.
    # A dict or list returned from a view will be converted to a JSON response automatically without needing to call this.
    json_e = jsonify(code=200, status=0, message='ok', value=data)
    print(json_e.json)  # print->{'code': 200, 'message': 'ok', 'status': 0, 'value': {'name': '您本次体检血压示:<b>150182 mmHg</b>。'}}
    return jsonify(code=200, status=0, message='ok', value=data)


if __name__ == '__main__':
    app.run(port=5000)
