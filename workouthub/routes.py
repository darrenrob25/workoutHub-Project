from flask import (
    flash, render_template, redirect, request, session, url_for, jsonify)
from werkzeug.security import generate_password_hash, check_password_hash
from workouthub import app, db
from workouthub.models import User, Workout, Exercise

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        if not username or not password:
            flash("Username and Password are required.", "danger")
            return redirect(url_for("home"))

        username = username.lower()
        existing_user = User.query.filter_by(username=username).first()

        if existing_user and check_password_hash(existing_user.password, password):
            session["user"] = username
            flash(f"Welcome Back, {username}", "success")
            return redirect(url_for("dashboard", username=username))
        else:
            flash("Incorrect Username or Password", "danger")

        return redirect(url_for("home"))

    return render_template("home.html")

@app.route("/dashboard/<username>", methods=["GET", "POST"])
def dashboard(username):
    if "user" not in session:
        return redirect(url_for("home"))

    user = User.query.filter_by(username=session.get("user")).first()
    if user:
        username = user.username
    else:
        return redirect(url_for("home"))

    return render_template("dashboard.html", username=username)

@app.route("/workouts", methods=["GET"])
def get_workouts():
    if "user" not in session:
        return jsonify({"error": "Not authorized"}), 403

    user = User.query.filter_by(username=session.get("user")).first()
    if not user:
        return jsonify({"error": "User not found"}), 404

    workouts = Workout.query.filter_by(user_id=user.id).all()
    workouts_data = []
    for workout in workouts:
        exercises = Exercise.query.filter_by(workout_id=workout.id).all()
        exercises_data = [{"exercise_name": e.exercise_name, "sets": e.sets, "reps": e.reps} for e in exercises]
        workouts_data.append({
            "workout_name": workout.workout_name,
            "workout_type": workout.workout_type,
            "exercises": exercises_data
        })

    return jsonify(workouts_data)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        
        if not username or not password:
            flash("Username and password are required", "danger")
            return redirect(url_for("register"))

        username = username.lower()
        existing_user = User.query.filter_by(username=username).first()

        if existing_user:
            flash("Username already in use", "danger")
            return redirect(url_for("register"))

        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        
        db.session.add(new_user)
        db.session.commit()

        session["user"] = username
        flash("Registration successful", "success")
        return redirect(url_for("home"))

    return render_template("register.html")

@app.route("/logout")
def logout():
    flash("Successfully Logged Out")
    session.clear()
    return redirect(url_for("home"))

@app.route("/add_workout", methods=["POST"])
def add_workout():
    if "user" not in session:
        flash("You must be logged in to add a workout.", "danger")
        return redirect(url_for("home"))

    user = User.query.filter_by(username=session.get("user")).first()
    if not user:
        flash("User not found.", "danger")
        return redirect(url_for("home"))

    workout_name = request.form.get("workout_name")
    workout_type = request.form.get("workout_type")
    exercise_names = request.form.getlist("exercise_name[]")
    sets = request.form.getlist("sets[]")
    reps = request.form.getlist("reps[]")

    if not workout_name or not workout_type:
        flash("Workout name and type are required.", "danger")
        return redirect(url_for("dashboard", username=user.username))

    new_workout = Workout(
        workout_name=workout_name,
        workout_type=workout_type,
        user_id=user.id
    )
    db.session.add(new_workout)
    try:
        db.session.commit()

        for exercise_name, set_count, rep_count in zip(exercise_names, sets, reps):
            new_exercise = Exercise(
                exercise_name=exercise_name,
                sets=set_count,
                reps=rep_count,
                workout_id=new_workout.id
            )
            db.session.add(new_exercise)

        db.session.commit()
        flash("Workout and exercises added successfully!", "success")
    except Exception as e:
        db.session.rollback()  # Rollback the session in case of an error
        flash(f"An error occurred: {str(e)}", "danger")

    return redirect(url_for("dashboard", username=user.username))