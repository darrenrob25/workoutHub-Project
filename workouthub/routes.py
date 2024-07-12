from flask import render_template
from workouthub import app, db
from workouthub.models import Workout, Exercise 


@app.route("/")
def home():
    return render_template("home.html") 

@app.route("/register", methods=["GET", "POST"])
def register():
    return render_template("register.html")