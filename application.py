from flask import Flask, render_template
import pymongo
app= Flask("_name_")
datos= [{"nombre":"Luis","edad":98}]
@app.route("/")
def index():
    return render_template("index.html",datos=datos)