from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello Flask,I am hello_world!"

@app.route("/hello")
def test():
    return "hello world!"

@app.route("/test")
def test2():
    return "hello test!"

@app.route("/test2")
def test3():
    return "hello test2!"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
