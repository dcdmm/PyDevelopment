from flask import Flask
from main import main

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def api_endpoint():
    result = main()
    result = str(result)
    return {"result": result}


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
