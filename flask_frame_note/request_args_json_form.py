from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/get_data/<int:num>', methods=['GET', 'POST'])
def example_get_post(num):
    if request.method == 'GET':
        print(num)  # print->print->1
        # test: GET 127.0.0.1:5000/get_data/1?name=frank&gender=male
        print(request.args)  # print->ImmutableMultiDict([('name', 'frank'), ('gender', 'male')])
        print(type(request.args))  # print->werkzeug.datastructures.ImmutableMultiDict
        name = request.args.get('name')
        gender = request.args.get('gender')
        return jsonify({'name': name, 'gender': gender})

    if request.method == 'POST':
        if request.headers.get('Content-Type') == 'application/json':
            """
            # test:
            POST 127.0.0.1:5000/get_data
            Content-Type: application/json
            name: dcdmm
            age: 100
            love: play_computer_game
            
            {
              "data": 123
            }
            """
            data_json = request.json
            print(data_json)  # print->{'data': 123}
            print(type(data_json))  # print->dict
            return jsonify(data_json)  # print->{"data":123}
        if request.headers.get('Content-Type') == 'application/x-www-form-urlencoded':
            """
            # test:
            ```
            POST http://127.0.0.1:5000/get_data
            Content-Type: application/x-www-form-urlencoded

            data=123  
            ```           
            """
            print(request.form)  # print->ImmutableMultiDict([('data', '123')])
            print(type(request.form))  # print->werkzeug.datastructures.ImmutableMultiDict
            print(request.form.get('data'))  # print->123
            return jsonify(request.form)  # print->{"data":"123"}


if __name__ == '__main__':
    app.run()
