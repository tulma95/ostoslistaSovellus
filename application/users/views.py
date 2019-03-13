from application import app, db
from flask import render_template, request, redirect, url_for
from application.users.models import User


@app.route("/users/new")
def usersForm():
    return render_template("users/new.html")


@app.route("/users/", methods=["GET"])
def usersIndex():
    return render_template("users/list.html", users=User.query.all())


@app.route("/users/", methods=["POST"])
def usersCreate():
    newUser = User(username=request.form.get("username"),
                   password=request.form.get("password"))

    db.session().add(newUser)
    db.session().commit()

    return redirect(url_for("usersIndex"))
