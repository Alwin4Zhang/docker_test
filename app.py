from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello Flask,I am hello_world!"

@app.route("/hello")
def hello():
    return "hello world!"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
