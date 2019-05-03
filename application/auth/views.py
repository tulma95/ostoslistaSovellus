
from flask import render_template, request, redirect, url_for
from flask_login import login_user, logout_user, current_user, login_required

from application import app, db
from application.auth.models import User
from application.groups.models import group_users
from application.auth.forms import LoginForm, RegisterForm


@app.route("/auth/info", methods=["POST", "GET"])
@login_required
def account_info():
    if request.method == "POST":
        User.remove_user(current_user.id)
        return redirect(url_for("index"))

    return render_template("auth/accountInfo.html")


@app.route("/auth/login", methods=["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form=LoginForm())

    form = LoginForm(request.form)

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

    try:
        newUser = User(name=form.name.data, username=form.username.data,
                       password=form.password.data)

        db.session().add(newUser)
        db.session().commit()
    except exc.IntegrityError:
        form.username.errors = ["That username is taken"]
        return render_template("auth/register.html", form=form)

    return redirect(url_for("auth_login"))


@app.route("/auth/logout")
@login_required
def auth_logout():
    logout_user()
    return redirect(url_for("index"))
