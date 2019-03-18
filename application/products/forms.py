from flask_wtf import FlaskForm
from wtforms import *


class ProductForm(FlaskForm):
    name = StringField("Product name", [validators.length(min=2, max=20)])

    class Meta:
        csrf = False
