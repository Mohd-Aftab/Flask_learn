from flask import Flask

app = Flask(__name__)

# API endppoints
@app.route('/')
def hello_world():
    return '<h1>Hello, World! I am AFTAB</h1>'

@app.route('/ping')
def ping():
    return {
        "message": "Why are you here? I am AFTAB",
    }