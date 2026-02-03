from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! from sukesh!!!!! Welcome to GitOps World !!!!"
