from flask import Flask , request , Response, render_template

app = Flask(__name__, template_folder='template')

@app.route("/")
def main():
    return "Hello this is the userless page"

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/submit", methods = ["POST"])
def submit():

    username = request.form.get("username")
    password = request.form.get("passw")

    if username == "jatin" and password =="123":
        return render_template("submit.html", name = username)
    else:
        return "invalid credential"
