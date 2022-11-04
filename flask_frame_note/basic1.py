from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)


@app.route('/get_data', methods=['GET', 'POST'])
def example_get():
    # http://127.0.0.1:5000/get_data?name=frank&gender=male
    if request.method == 'GET':
        name = request.args.get('name')
        gender = request.args.get('gender')
        return jsonify({'name': name, 'gender': gender})

    # curl -H "Content-Type: application/json" http://127.0.0.1:5000/get_data -d '{"data":123}' -X POST
    if request.method == 'POST':
        data_json = request.json
        return jsonify(data_json)


if __name__ == '__main__':
    app.run()
