from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField


class LoginForm(FlaskForm):
    username = StringField("Username")
    password = StringField("Password")

    class Meta:
        csrf = False
