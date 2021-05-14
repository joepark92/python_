from flask import render_template, redirect, request, session, flash, url_for

from flask_app import app
from ..models.dojo import Dojo


@app.route("/")
def redirectroute():

    return redirect('/dojos')


#read many dojos
@app.route("/dojos")
def index():
    dojos = Dojo.get_all_dojos()

    return render_template("index.html", all_dojos = dojos)


#read one dojo
@app.route("/dojos/<int:dojo_id>")
def display_dojo(dojo_id):
    # data = {
    #     "id": dojo_id
    # }
    this_dojo = Dojo.get_dojo_ninjas({"id": dojo_id})

    return render_template("dojo.html", dojo = this_dojo)


#create a dojo
@app.route("/dojos/create", methods = ["POST"])
def createdojo():
    Dojo.create(request.form)

    return redirect("/")
