from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required

from application import app, db
from application.groups.models import Group
from application.groups.forms import GroupForm
from application.products.models import Product

from application.products.forms import ProductForm


@app.route("/groups/")
@login_required
def groups_index():
    return render_template("groups/list.html",
                           groups=Group.query.all(),
                           form=GroupForm())


@app.route("/groups/<groupId>/")
def group_page(groupId):

    print("-----------------------------------------------")
    print(request.args.get("error"))

    return render_template("products/list.html",
                           products=Product.query.all(),
                           group=Group.query.get(groupId),
                           form=ProductForm(),
                           error=request.args.get("error"))


@app.route("/groups/new", methods=["POST"])
@login_required
def groups_create():
    form = GroupForm(request.form)

    """if not form.validate():
        print("VIRHEET ----------------------------")
        print(form.name.errors)
        print("-------------------------------------")
        return render_template("groups/list.html",
                               groups=Group.query.all(),
                               form=form)"""

    newGroup = Group(name=form.name.data,
                     groupCreator=current_user.username)

    db.session().add(newGroup)
    db.session().commit()
    return redirect(url_for("groups_index"))
