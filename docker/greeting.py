from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1 style='color:green'>Greetings from Docker version 2.0!</h1>"
