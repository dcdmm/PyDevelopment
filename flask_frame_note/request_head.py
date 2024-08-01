from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/get_data', methods=['POST'])
def example_get():
    """
    # test:
    ```
    POST 127.0.0.1:5000/get_data
    Content-Type: application/json
    name: dcdmm
    age: 100
    love: play_computer_game

    {
        "key": "value"
    }
    ```
    """
    print("Content-Type", request.headers.get('Content-Type'))  # print->application/json
    print("name", request.headers.get('name'))  # print->dcdcmm
    print("age", request.headers.get('age'))  # print->100
    print("love", request.headers.get('love'))  # print->play_computer_game
    return jsonify({"result": "ok"})


if __name__ == '__main__':
    app.run()
