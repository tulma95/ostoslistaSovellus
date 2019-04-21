
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user

from application import app, db
from application.auth.models import User
from application.groups.models import group_users
from application.auth.forms import LoginForm, RegisterForm

from sqlalchemy.sql import text


@app.route("/auth/info", methods=["POST", "GET"])
def account_info():

    if request.method == "POST":
        stmt = text('''
        DELETE FROM group_users WHERE account_id = :accountId;'''
                    ).params(accountId=current_user.id)

        res = db.engine.execute(stmt)
        User.query.filter_by(id=current_user.id).delete()
        db.session().commit()
        return redirect(url_for("index"))

    return render_template("auth/accountInfo.html")


@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(
        username=form.username.data, password=form.password.data).first()
    if not user:
        return render_template("auth/loginform.html", form=form,
                               error="No such username or password")

    login_user(user)
    return redirect(url_for("index"))


@app.route("/auth/register")
def auth_register():
    return render_template("auth/register.html", form=RegisterForm())


@app.route("/auth/", methods=["POST"])
def auth_createUser():
    form = RegisterForm(request.form)

    if not form.validate():
        return render_template("auth/register.html", form=form)

    newUser = User(name=form.name.data, username=form.username.data,
                   password=form.password.data)

    db.session().add(newUser)
    db.session().commit()

    return redirect(url_for("auth_login"))


@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index"))
