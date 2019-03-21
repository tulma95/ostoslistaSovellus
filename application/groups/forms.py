from flask_wtf import FlaskForm
from wtforms import *


class GroupForm(FlaskForm):
    name = StringField("new group name", [validators.length(min=2, max=20)])

    class meta:
        csrf: False
