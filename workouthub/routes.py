from flask import (
    flash, render_template,
    redirect, request, session, url_for)
from werkzeug.security import generate_password_hash, check_password_hash
from workouthub import app, db
from workouthub.models import User, Workout, Exercise


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if not username or not password:
            flash("Username and password are required")
            return redirect(url_for("register"))

        username = username.lower()

        # Checking to see if username is unique
        existing_user = User.query.filter_by(username=username).first()

        if existing_user:
            flash("Username already in use")
            return redirect(url_for("register"))

        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        
        db.session.add(new_user)
        db.session.commit()

        # Put the new user into session
        session["user"] = username
        flash("Registration successful")
        return redirect(url_for("home"))

    return render_template("register.html")