from flask import render_template
from workouthub import app, db
from workouthub.models import Workout, Exercise 


@app.route("/")
def home():
    return render_template("home.html") 