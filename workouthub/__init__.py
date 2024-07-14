import os 
from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env
from sqlalchemy.pool import QueuePool

app.config["SQLALCHEMY_ENGINE_OPTIONS"] = {
    "pool_size": 5,        
    "max_overflow": 10,     
    "pool_timeout": 30     
}

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY")

if os.environ.get("DEVELOPMENT") == "True":
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DB_URL")
else: 
    uri = os.environ.get("DATABASE_URL")
    if uri.startswith("postgres://"):
         uri = uri.replace("postgres://", "postgresql://", 1)
    app.config["SQLALCHEMY_DATABASE_URI"] = uri

db = SQLAlchemy(app)

from workouthub import routes