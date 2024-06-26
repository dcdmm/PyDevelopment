from flask import Flask, jsonify

app = Flask(__name__)
# Serialize objects to ASCII-encoded JSON. If this is disabled, the JSON returned from jsonify will contain Unicode characters.
app.json.ensure_ascii = False  # 通过设置app.json.ensure_ascii = False,使其正常显示中文


@app.route('/index')
def index():
    data = {
        'name': '您本次体检血压示:<b>150182 mmHg</b>。'
    }

    # Serialize data to JSON and wrap it in a :class:`~flask.Response
    return jsonify(code=200, status=0, message='ok', value=data)


if __name__ == '__main__':
    app.run(port=5000)
