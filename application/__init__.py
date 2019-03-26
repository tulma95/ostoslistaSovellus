from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

import os


if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"    
    app.config["SQLALCHEMY_ECHO"] = True
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True


db = SQLAlchemy(app)

from application import views

from application.products import models
from application.products import views

from application.auth import models
from application.auth import views

from application.groups import models
from application.groups import views


# kirjautuminen
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
loginManager = LoginManager()
loginManager.init_app(app)

loginManager.login_view = "auth_login"
loginManager.login_message = "Please login to use this functionality"

@loginManager.user_loader
def loadUser(userId):
    return User.query.get(userId)

try: 
    db.create_all()
except:
    pass