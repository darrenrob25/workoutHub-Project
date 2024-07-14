# Importing modules and functions
import os 
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


# Check if the env.py file exists for environment settings
if os.path.exists("env.py"):
    import env

# Importing QueuePool class from sqlalchemy
from sqlalchemy.pool import QueuePool


# Create the flask application
app = Flask(__name__)

# Configure the flask app with the secret key
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")


if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else: 
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
         uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri


db = SQLAlchemy(app)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()


from workouthub import routes