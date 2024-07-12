from flask import (
    flash, render_template,
    redirect, request, session, url_for)
from werkzeug.security import generate_password_hash, check_password_hash
from workouthub import app, db
from workouthub.models import User, Workout, Exercise


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        # Get the username and password from the form
        username = request.form.get("username")
        password = request.form.get("password")

        # Check if the username and password are provided
        if not username or not password:
            flash("Username and Password are required.", "danger")
            return redirect(url_for("home"))

        username = username.lower()  # Ensure username is in lowercase

        # Fetch the user from the database
        existing_user = User.query.filter_by(username=username).first()

        if existing_user:
            # Check if the password matches
            if check_password_hash(existing_user.password, password):
                session["user"] = username
                flash(f"Welcome Back, {username}", "success")
                return redirect(url_for("home"))
            else:
                # Incorrect password
                flash("Incorrect Username or Password", "danger")
        else:
            # Username doesn't exist
            flash("Incorrect Username or Password", "danger")

        return redirect(url_for("home"))

    return render_template("home.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if not username or not password:
            flash("Username and password are required", "danger")
            return redirect(url_for("register"))

        username = username.lower()

        # Checking to see if username is unique
        existing_user = User.query.filter_by(username=username).first()

        if existing_user:
            flash("Username already in use", "danger")
            return redirect(url_for("register"))
        #hashing password for security
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        
        db.session.add(new_user)
        db.session.commit()

        # Put the new user into session
        session["user"] = username
        flash("Registration successful", "success")
        return redirect(url_for("home"))

    return render_template("register.html")