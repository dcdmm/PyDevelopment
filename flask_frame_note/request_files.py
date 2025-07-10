import os
from flask import Flask, request

app = Flask(__name__)


@app.route('/upload', methods=['POST'])
def upload_file():
    print(request.files)
    print(request.files.getlist('file'))
    for file in request.files.getlist('file'):
        print(file.filename)

        file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "./data")
        file_path = os.path.join(file_path, "_" + file.filename)
        print(file_path)
        file.save(file_path)

        content = file.read().decode('utf-8')
        print(content)
    return "<p>ok!</p>"


if __name__ == '__main__':
    app.run()
