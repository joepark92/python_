from flask_app.config.mysqlconnection import connectToMySQL
from flask import render_template, redirect, request, session, flash

from flask_app import app
from ..models.survey import Survey


@app.route("/")
def dojo_form():
    return render_template("index.html")


@app.route("/result", methods = ['POST'])
def dojo_create():

    if not Survey.validate_survey(request.form):
        return redirect("/")
        
    Survey.create_survey(request.form)

    user_id = Survey.create_survey(request.form)

    return redirect(f"/result/{user_id}")


@app.route("/result/<int:user_id>")
def survey_result(user_id):
    data = {
        "id": user_id
    }
    user_id = Survey.dojo_result(data)

    return render_template("show.html", survey = user_id)
