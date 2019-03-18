from application.auth import models
from application.products import views
from application.products import models
from application import views
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_ECHO"] = True
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

db = SQLAlchemy(app)


db.create_all()
