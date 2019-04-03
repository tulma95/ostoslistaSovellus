from flask_wtf import FlaskForm
from wtforms import *


class UserListForm(FlaskForm):
    username = SelectField('username', choices=[])

    class meta:
        csrf: False


class GroupForm(FlaskForm):
    name = StringField("new group name", [validators.length(min=2, max=20)])

    class meta:
        csrf: False
