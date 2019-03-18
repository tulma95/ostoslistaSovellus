from flask_wtf import FlaskForm
from wtforms import *

class ProductForm(FlaskForm):
    name = StringField("Product name")

    class Meta:
        csrf = False