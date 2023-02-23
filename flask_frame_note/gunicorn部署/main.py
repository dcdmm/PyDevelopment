from flask import Flask

app = Flask(__name__)


@app.route('/index')
def index():
    return 'hello world'

'''
gunicorn介绍:
What is WSGI?
WSGI is the Web Server Gateway Interface. It is a specification that describes how a web server communicates with web applications, and how web applications can be chained together to process one request.

WSGI is a Python standard described in detail in PEP 3333(https://www.python.org/dev/peps/pep-3333).

For more, see Learn about WSGI(https://www.python.org/dev/peps/pep-3333).

Gunicorn 'Green Unicorn' is a Python WSGI HTTP Server for UNIX. It's a pre-fork worker model. 
The Gunicorn server is broadly compatible with various web frameworks, simply implemented, light on server resources, and fairly speedy.
'''
# gunicorn部署flask:
# Linux:gunicorn -c conf/gunicorn.py main:app
# docker:CMD ["gunicorn", "-c", "conf/gunicorn.py", "main:app"]
if __name__ == '__main__':
    app.run(debug=True)
