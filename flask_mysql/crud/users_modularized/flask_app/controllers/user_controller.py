from flask import render_template, redirect, request, session, flash

from flask_app import app
from ..models.user import User

@app.route("/")
def redirectroute():
    return redirect('/users')

# READ Many
@app.route("/users")
def index():
    users = User.get_all_users()

    return render_template("index.html", all_users = users)


# READ One
@app.route("/users/<int:user_id>")
def display_user(user_id):
    data = {
        "id": user_id
    }
    this_user = User.get_one_user(data)

    return render_template("user.html", user = this_user)

# CREATE
@app.route("/users/new")
def new_user_form():
    return render_template("create.html")



@app.route("/users/create", methods = ["POST"])
def create():
    User.create(request.form)
    
    return redirect("/")


# UPDATE
@app.route("/users/<int:user_id>/edit")
def edit_user_form(user_id):
    data = {
        "id": user_id
    }

    user_list = User.edit_user_form(data)

    return render_template("edit.html", user = user_list)


@app.route("/users/<int:user_id>/update", methods = ["POST"])
def update_user(user_id):
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "id": user_id
    }
    User.update_user(data)

    return redirect("/")


# DELETE
@app.route("/users/<int:user_id>/delete")
def delete_user(user_id):
    data = {
        "id": user_id
    }
    User.delete_user(data)

    return redirect("/")