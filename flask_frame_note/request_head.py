from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/get_data', methods=['POST'])
def example_get():
    """
    # test:
    curl  'http://127.0.0.1:5000/get_data' \
    --header 'Content-Type: application/json' \
    -H 'name: dcdmm' \
    -H 'age: 100' \
    -H 'love: play_computer_game' \
    --data '{"key": "value"}'
    """
    print("Content-Type", request.headers.get('Content-Type'))  # application/json
    print("name", request.headers.get('name'))  # dcdcmm
    print("age", request.headers.get('age'))  # 100
    print("love", request.headers.get('love'))  # play_computer_game
    return jsonify({"result": "ok"})


if __name__ == '__main__':
    app.run()
