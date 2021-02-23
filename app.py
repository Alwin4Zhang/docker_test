from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world"

@app.route("/hello")
def hello_flask():
    return {"result":"Hello flask!"}

if __name__ == '__main__':
    app.run(host="0.0.0.0")
    