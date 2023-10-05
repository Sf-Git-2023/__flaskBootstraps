from flask import Flask,render_template


app = Flask(__name__)

@app.route("/")
def index():
    names = ['徐國堂','李亦宣','林冠宏','陳宇哲']    
    return render_template("index.jinja.html",names=names)

@app.route("/feature")
def feature():
    return render_template("feature.jinja.html")

@app.route("/description")
def description():
    return render_template("description.jinja.html")

@app.route("/product")
def product():
    return render_template("product.jinja.html")