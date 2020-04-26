from flask import Flask
app = Flask(__name__)
@app.route("/")
def homepage():
    return("Placeholder homepage text")
