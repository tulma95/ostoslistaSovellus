from flask import render_template, request, redirect, url_for
from flask_login import login_required

from application import app, db
from application.products.models import Product
from application.products.forms import ProductForm


@app.route("/products/", methods=["GET"])
def products_list():
    return render_template("products/list.html",
                           products=Product.query.all())


@app.route("/products/new")
@login_required
def products_form():
    return render_template("products/new.html", form=ProductForm())


@app.route("/products/<productId>/", methods=["POST"])
@login_required
def product_add(productId):
    p = Product.query.get(productId)
    p.count = p.count + 1
    db.session().commit()

    return redirect(url_for("products_list"))


@app.route("/decrease/<productId>/", methods=["POST"])
@login_required
def product_decrease(productId):
    p = Product.query.get(productId)
    p.count = p.count - 1
    db.session().commit()

    return redirect(url_for("products_list"))


@app.route("/products/", methods=["POST"])
@login_required
def products_create():
    form = ProductForm(request.form)

    if not form.validate():
        return render_template("products/new.html", form=form)

    newProduct = Product(name=form.name.data,
                         count=1)

    db.session().add(newProduct)
    db.session().commit()

    return redirect(url_for("products_list"))
