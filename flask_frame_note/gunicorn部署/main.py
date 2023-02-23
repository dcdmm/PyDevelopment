from flask import Flask

app = Flask(__name__)


@app.route('/index')
def index():
    return 'hello world'

# gunicorn部署flask:
# Linux:gunicorn -c conf/gunicorn.py main:app
# docker:CMD ["gunicorn", "-c", "conf/gunicorn.py", "main:app"]
if __name__ == '__main__':
    app.run(debug=True)
