from flask import render_template, redirect, request, session, flash, url_for

from flask_app import app
from ..models.ninja import Ninja
from ..models.dojo import Dojo


@app.route("/ninjas")
def new_ninja_form():
    dojo = Dojo.get_all_dojos()

    return render_template("ninja.html", all_dojos = dojo)


@app.route("/ninjas/create", methods = ['POST'])
def create_ninja():
    Ninja.create(request.form)
    dojoid = request.form['dojo_id']

    return redirect(f"/dojos/{dojoid}")

#delete ninja from dojo
@app.route("/ninjas/<int:dojo_id>/<int:ninja_id>/delete")
def delete_ninja(dojo_id, ninja_id):
    data = {
        "id": ninja_id,
    }

    Ninja.delete_ninja(data)

    return redirect(f"/dojos/{dojo_id}")