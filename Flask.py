from flask import Flask
app = Flask(__name__)


@app.route('/<name>/<age>')
def hello(name,age):

    return "Hello World!" + name +" "+ age
