from flask import render_template, request, redirect, url_for
from flask_login import current_user, login_required

from application import app, db
from application.groups.models import Group
from application.groups.forms import GroupForm, UserListForm
from application.auth.models import User
from application.products.models import Product

from application.products.forms import ProductForm


@app.route("/groups/<groupId>/info/deleteuser", methods=["POST", "GET"])
@login_required
def group_delete_user(groupId):
    group = Group.query.get(groupId)
    group.users.remove(current_user)
    db.session().commit()

    return redirect(url_for("groups_index"))


@app.route("/groups/<groupId>/delete", methods=["POST"])
@login_required
def group_delete(groupId):
    Group.delete_group(groupId)
    return redirect(url_for("groups_index"))


@app.route("/groups/<groupId>/info", methods=["POST", "GET"])
@login_required
def group_info(groupId):
    group = Group.query.get(groupId)
    userlistForm = UserListForm()

    if request.method == "POST":
        group.users.append(User.query.get(userlistForm.username.data))
        db.session().commit()

    usersNotInGroup = Group.find_users_not_in_group(groupId)

    userlistForm.username.choices = [
        (user.id, user.name) for user in usersNotInGroup]

    return render_template("groups/groupInfo.html",
                           users=Group.query.get(groupId).users,
                           form=userlistForm,
                           groupId=groupId,
                           group=group)


@app.route("/groups/")
@login_required
def groups_index():
    groups = Group.find_user_groups_and_item_count(current_user.id)
    return render_template("groups/list.html",
                           groups=groups,
                           form=GroupForm())


@app.route("/groups/<groupId>/")
@login_required
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

    if not form.validate():
        print('----------------------------22-')
        groups = Group.find_user_groups_and_item_count(current_user.id)
        return render_template("groups/list.html",
                               groups=groups,
                               form=form)

    newGroup = Group(name=form.name.data,
                     groupCreator=current_user.username)

    db.session().add(newGroup)
    newGroup.users.append(current_user)
    db.session().commit()
    print('----------------------------')
    return redirect(url_for("groups_index"))
