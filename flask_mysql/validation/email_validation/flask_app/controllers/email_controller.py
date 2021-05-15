from flask import render_template, redirect, request, session, flash
from flask_app.config.mysqlconnection import connectToMySQL

from flask_app import app
from ..models.email import Email


import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/add", methods = ['POST'])
def input_email():
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid email address. Enter a valid email.")
        return redirect("/")

    for x in Email.email_list():
        if request.form['email'] == x['email']:
            flash("This email address is already in use.")
            return redirect("/")

    email_id = Email.add_email(request.form)

    return redirect(f"/success/{email_id}")


@app.route("/success/<int:email_id>")
def success(email_id):
    data = {
        "id": email_id
    }
    email_id = Email.email_one(data)
    email_id_all = Email.email_list()
    return render_template("success.html", email = email_id, emails = email_id_all)


@app.route("/delete/<int:email_id>")
def delete(email_id):
    data = {
        'id': email_id
    }
    Email.delete(data)

    return redirect("/")