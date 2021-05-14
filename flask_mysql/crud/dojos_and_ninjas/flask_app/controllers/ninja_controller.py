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

    return redirect(url_for(".display_dojo", dojo_id = dojoid))

#delete ninja from dojo
@app.route("/ninjas/<int:ninja_id>/delete")
def delete_ninja(ninja_id):
    data = {
        "id": ninja_id,
    }

    Ninja.delete_ninja(data)

    return redirect("/dojos")