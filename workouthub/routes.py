# Importing modules and functions from Flask and other libraries
from flask import (
    flash, render_template, redirect, request, session, url_for, jsonify
)
from werkzeug.security import generate_password_hash, check_password_hash
from workouthub import app, db
from workouthub.models import User, Workout, Exercise


# Route for the home page, handles both GET and POST requests
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        # checking that both username and password are provided
        if not username or not password:
            flash("Username and Password are required.", "danger")
            return redirect(url_for("home"))

        # converting username to lowercase for consistency.
        username = username.lower()
        #checking if the user exists and existing password is correct
        existing_user = User.query.filter_by(username=username).first()
        if existing_user and check_password_hash(existing_user.password, password):
            # If the login is successful, store the username in the session and redirect to dashboard
            session["user"] = username
            flash(f"Welcome Back, {username}", "success")
            return redirect(url_for("dashboard", username=username))
        else:
            flash("Incorrect Username or Password", "danger")

        return redirect(url_for("home"))
    # rendering the homepage template
    return render_template("home.html")


# Route for the dashboard page, shows the users workouts
@app.route("/dashboard/<username>", methods=["GET", "POST"])
def dashboard(username):
    if "user" not in session:
        return redirect(url_for("home"))

    # Gets the user based on the username stored in the session
    user = User.query.filter_by(username=session.get("user")).first()
    if user:
        username = user.username
    else:
        return redirect(url_for("home"))

    # Get all workouts associated with the user
    workouts = Workout.query.filter_by(user_id=user.id).all()
    workouts_data = []
    for workout in workouts:
        # Get exercises for each workout
        exercises = Exercise.query.filter_by(workout_id=workout.id).all()
        exercises_data = [{"exercise_name": e.exercise_name, "sets": e.sets, "reps": e.reps} for e in exercises]
        workouts_data.append({
            "id": workout.id,  # Makes sure id is included for edit links
            "workout_name": workout.workout_name,
            "workout_type": workout.workout_type,
            "exercises": exercises_data
        })

    # Renders the dashboard template with the users workouts
    return render_template("dashboard.html", username=username, workouts=workouts_data)

# Route for registration page, allowing GET and POST
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        

        # Check if both username and password are provided
        if not username or not password:
            flash("Username and password are required", "danger")
            return redirect(url_for("register"))

        # Converting username to lowercase
        username = username.lower()
        # Checking if username already exists
        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash("Username already in use", "danger")
            return redirect(url_for("register"))

        # Hashing password before storing it for security
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        
        # Adding new user to the database and committing
        db.session.add(new_user)
        db.session.commit()


        # Log the user in and redirect to the home page
        session["user"] = username
        flash("Registration successful", "success")
        return redirect(url_for("home"))

    # Renders the registration template
    return render_template("register.html")


# Route for logging out, clears the session and redirects to home page
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

@app.route("/delete_workout/<int:workout_id>", methods=["POST"])
def delete_workout(workout_id):
    if "user" not in session:
        flash("You must be logged in to delete a workout.", "danger")
        return redirect(url_for("home"))

    user = User.query.filter_by(username=session.get("user")).first()
    if not user:
        flash("User not found.", "danger")
        return redirect(url_for("home"))

    workout = Workout.query.get_or_404(workout_id)

    if workout.user_id != user.id:
        flash("You do not have permission to delete this workout.", "danger")
        return redirect(url_for("dashboard", username=user.username))

    db.session.delete(workout)
    db.session.commit()
    flash("Workout deleted successfully!", "success")
    return redirect(url_for("dashboard", username=user.username))

@app.route("/edit-workout/<int:workout_id>", methods=["GET", "POST"])
def edit_workout(workout_id):
    workout = Workout.query.get_or_404(workout_id)
    
    if request.method == "POST":
        workout_name = request.form.get("workout_name")
        workout_type = request.form.get("workout_type")
        exercise_ids = request.form.getlist("exercise_id[]")
        exercise_names = request.form.getlist("exercise_name[]")
        sets = request.form.getlist("sets[]")
        reps = request.form.getlist("reps[]")

        if not workout_name or not workout_type:
            flash("Workout name and type are required.", "danger")
            return redirect(url_for("edit_workout", workout_id=workout_id))
        
        workout.workout_name = workout_name
        workout.workout_type = workout_type

        try:
            # Clear existing exercises
            Exercise.query.filter_by(workout_id=workout.id).delete()

            # Add updated exercises
            for exercise_name, set_count, rep_count in zip(exercise_names, sets, reps):
                new_exercise = Exercise(
                    exercise_name=exercise_name,
                    sets=set_count,
                    reps=rep_count,
                    workout_id=workout.id
                )
                db.session.add(new_exercise)

            db.session.commit()
            flash("Workout updated successfully!", "success")
            return redirect(url_for("dashboard", username=session.get("user")))
        except Exception as e:
            db.session.rollback()
            flash(f"An error occurred: {str(e)}", "danger")
            return redirect(url_for("edit_workout", workout_id=workout_id))
    
    return render_template("edit_workout.html", workout=workout)