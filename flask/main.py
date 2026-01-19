from flask import Flask , request

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello this is the homepage"

@app.route("/contact")
def contact():
    return "this is contacts"

@app.route("/submit", methods = ["GET", "POST"])
def submit():
    if request.method == "GET":
        return "get the data here"
    else:
        return "submit data"
