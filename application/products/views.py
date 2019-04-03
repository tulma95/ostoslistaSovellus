from flask import render_template, request, redirect, url_for
from flask_login import login_required

from application import app, db
from application.products.models import Product
from application.products.forms import ProductForm


@app.route("/products/", methods=["GET"])
def products_list():
    return render_template("products/list.html",
                           products=Product.query.all())

@app.route("/products/remove/<productId>/<groupId>", methods=["POST"])
def product_remove(productId, groupId):
    Product.query.filter_by(id=productId).delete()
    db.session().commit()
    return redirect(url_for("group_page", groupId=groupId))

@app.route("/products/new")
@login_required
def products_form():
    return render_template("products/new.html", form=ProductForm())


@app.route("/products/<productId>/<groupId>", methods=["POST"])
@login_required
def product_add(productId, groupId):
    p = Product.query.get(productId)
    p.count = p.count + 1
    db.session.commit()

    return redirect(url_for("group_page", groupId=groupId))


@app.route("/decrease/<productId>/<groupId>/", methods=["POST"])
@login_required
def product_decrease(productId, groupId):
    p = Product.query.get(productId)
    p.count = p.count - 1
    db.session.commit()

    return redirect(url_for("group_page", groupId=groupId))


@app.route("/products/<groupId>", methods=["POST"])
@login_required
def products_create(groupId):
    form = ProductForm(request.form)

    if not form.validate():
        return redirect(url_for("group_page", groupId=groupId, error=form.name.errors))

    newProduct = Product(name=form.name.data,
                         count=1,
                         groupId=groupId)

    db.session().add(newProduct)
    db.session().commit()

    return redirect(url_for("group_page", groupId=groupId))
