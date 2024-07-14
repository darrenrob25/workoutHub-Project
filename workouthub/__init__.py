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

# SQLAlchemy settings
app.config['SQLALCHEMY_POOL_SIZE'] = 10  # Adjust based on your database's connection limit and app's needs
app.config['SQLALCHEMY_MAX_OVERFLOW'] = 5  # Adjust based on your expected peak load
app.config['SQLALCHEMY_POOL_TIMEOUT'] = 30  # Timeout in seconds for acquiring a connection from the pool
app.config['SQLALCHEMY_POOL_RECYCLE'] = 3600  # Recycle connections after this many seconds to avoid timeouts and stale connections


db = SQLAlchemy(app)


@app.teardown_appcontext
def shutdown_session(exception=None):
    db.session.remove()


from workouthub import routes