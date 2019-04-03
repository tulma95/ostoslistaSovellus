from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required

from application import app, db
from application.groups.models import Group
from application.groups.forms import GroupForm
from application.products.models import Product

from application.products.forms import ProductForm


@app.route("/groups/<groupId>/info")
def group_info(groupId):
    return render_template("groups/groupInfo.html",
                           users=Group.query.get(groupId).users)


@app.route("/groups/")
@login_required
def groups_index():
    return render_template("groups/list.html",
                           groups=Group.query.all(),
                           form=GroupForm())


@app.route("/groups/<groupId>/")
def group_page(groupId):

    return render_template("products/list.html",
                           products=Product.query.filter_by(groupId=groupId),
                           group=Group.query.get(groupId),
                           form=ProductForm(),
                           error=request.args.get("error"))


@app.route("/groups/new", methods=["POST"])
@login_required
def groups_create():
    form = GroupForm(request.form)
    newGroup = Group(name=form.name.data,
                     groupCreator=current_user.username)

    db.session().add(newGroup)
    newGroup.users.append(current_user)
    db.session().commit()
    return redirect(url_for("groups_index"))
