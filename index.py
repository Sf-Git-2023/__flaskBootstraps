from flask import Flask,render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.jinja.html")

@app.route("/feature")
def feature():
    return render_template("feature.jinja.html")


