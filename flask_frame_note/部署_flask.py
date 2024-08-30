from flask import Flask

app = Flask(__name__)


@app.route("/", methods=['GET'])
def root():
    return {"message": "Hello World"}

# h, --host TEXT        The interface to bind to.
# -p, --port INTEGER        he port to bind to.
# 命令行: `flask --app 部署_flask:app run --host 0.0.0.0 --port 5001`
