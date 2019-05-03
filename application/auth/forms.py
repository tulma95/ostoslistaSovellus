from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators


class LoginForm(FlaskForm):
    username = StringField("Username")
    password = PasswordField("Password")

    class Meta:
        csrf = False


class ChangeUsernameForm(FlaskForm):
    username = StringField("New username", [validators.length(min=4, max=12)])

    class Meta:
        csrf = False


class RegisterForm(FlaskForm):
    name = StringField("Name")
    username = StringField("Username", [validators.length(min=4, max=12)])
    password = PasswordField("Password", [validators.length(min=4, max=12)])
    confirm = PasswordField("Repeat password",
                            [validators.EqualTo('password', message="Passwords must match")])

    class Meta:
        csrf = False
