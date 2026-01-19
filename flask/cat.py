from flask import Flask , render_template
import requests

app = Flask(__name__ , template_folder= "template")

@app.route("/")
def cats():
    response = requests.get('https://api.thecatapi.com/v1/images/search')
    cat_url = response.json()[0]['url']
    print(response.json())
    return render_template ("cat.html", cat_url=cat_url)
