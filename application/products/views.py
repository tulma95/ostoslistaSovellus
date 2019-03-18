from application import app, db
from flask import render_template, request, redirect, url_for
from application.products.models import Product
from application.products.forms import ProductForm

@app.route("/products/new")
def productsForm():
    return render_template("products/new.html", form = ProductForm())


@app.route("/products/<productId>/", methods=["POST"])
def productAdd(productId):
    p = Product.query.get(productId)
    p.count = p.count + 1
    db.session().commit()

    return redirect(url_for("productsList"))


@app.route("/decrease/<productId>/", methods=["POST"])
def productDecrease(productId):
    p = Product.query.get(productId)
    p.count = p.count - 1
    db.session().commit()

    return redirect(url_for("productsList"))


@app.route("/products/", methods=["GET"])
def productsList():
    return render_template("products/list.html",
                           products=Product.query.all())


@app.route("/products/", methods=["POST"])
def productsCreate():
    newProduct = Product(name=request.form.get("name"),
                         count=1)

    db.session().add(newProduct)
    db.session().commit()

    return redirect(url_for("productsList"))
