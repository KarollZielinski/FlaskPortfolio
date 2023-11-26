from portfolio import app
from flask import render_template, url_for

@app.get("/")
def index():
    return render_template("index.html")