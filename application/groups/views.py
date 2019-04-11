from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required

from application import app, db
from application.groups.models import Group
from application.groups.forms import GroupForm, UserListForm
from application.auth.models import User
from application.products.models import Product
from sqlalchemy.sql import *

from application.products.forms import ProductForm


@app.route("/groups/<groupId>/info/deleteuser", methods=["POST", "GET"])
def group_delete_user(groupId):
    group = Group.query.get(groupId)
    group.users.remove(current_user)
    db.session().commit()

    return redirect(url_for("groups_index", groupId=groupId))


@app.route("/groups/<groupId>/info", methods=["POST", "GET"])
def group_info(groupId):
    userList = User.query.all()
    group = Group.query.get(groupId)
    # query = db.session.query(User).join(
    #     Group.users).filter(User.id.notin_(Group_users)

    # q = User.query.filter(Group.query.get(groupId))

    print('--------')
    print(group.groupCreator)

    # filtered = User.query.filter(User.id.in_(Group.query.get(groupId).users))
    # print('-------------------')
    # print(filtered)
    # usersInGroup = Group.query.get(groupId).users

    userlistForm = UserListForm()
    userlistForm.username.choices = [(user.id, user.name) for user in userList]

    if request.method == "POST":
        group = Group.query.get(groupId)
        group.users.append(User.query.get(userlistForm.username.data))
        db.session().commit()

    return render_template("groups/groupInfo.html",
                           users=Group.query.get(groupId).users,
                           form=userlistForm,
                           groupId=groupId,
                           group=group)


@app.route("/groups/")
@login_required
def groups_index():

    query = db.session.query(Group).join(
        Group.users).filter(User.id == current_user.id)

    return render_template("groups/list.html",
                           groups=query,
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
