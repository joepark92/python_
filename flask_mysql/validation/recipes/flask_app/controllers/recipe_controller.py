from flask import render_template, request, redirect, session

from flask_app import app
from ..models.user import User
from ..models.recipe import Recipe


@app.route("/dashboard")
def dashboard():
    if 'uuid' not in session:
        return redirect("/")

    return render_template("dashboard.html", user = User.get_user_id({"id": session['uuid']}))


@app.route("/recipes/new")
def new_recipe():
    if 'uuid' not in session:
        return redirect("/")

    return render_template("new_recipe.html", user = User.get_user_id({"id": session['uuid']}))


@app.route("/recipes/create", methods = ['POST'])
def create_recipe():
    if not Recipe.validator(request.form):
        return redirect("/recipes/new")

    data = {
        "user_id": session['uuid'],
        "name": request.form['name'],
        "description": request.form['description'],
        "instruction": request.form['instruction'],
        "under": request.form['under']
    }
    Recipe.create(data)

    return redirect("/dashboard")


@app.route("/recipes/<int:id>")
def display_recipe(id):
    if 'uuid' not in session:
        return redirect("/")
    
    return render_template("show_recipe.html", recipe = Recipe.get_one({"id": id}))


@app.route("/recipes/<int:id>/edit")
def edit_ice_cream(id):
    if 'uuid' not in session:
        return redirect("/")

    return render_template(
        "edit_recipe.html",
        recipe = Recipe.get_one({"id": id}),
        user = User.get_user_id({"id": session['uuid']})
    )

#update
@app.route("/recipes/<int:id>/update", methods = ['POST'])
def update_recipe(id):
    if not Recipe.validator(request.form):
        return redirect(f"/recipes/{id}/edit")

    data = {
        "name": request.form['name'],
        "description": request.form['description'],
        "instruction": request.form['instruction'],
        "under": request.form['under'],
        "id": id
    }
    Recipe.update(data)

    return redirect("/dashboard")



@app.route("/recipes/<int:id>/delete")
def delete_recipe(id):
    Recipe.delete({"id": id})

    return redirect("/dashboard")