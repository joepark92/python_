from flask import render_template, request, redirect, session

from flask_app import app
from ..models.user import User
from ..models.car import Car


@app.route("/dashboard")
def dashboard():
    if 'uuid' not in session:
        return redirect("/")

    return render_template(
        "dashboard.html", 
        user = User.get_user_id({"id": session['uuid']}), 
        all_cars = Car.get_all()
    )


@app.route("/cars")
def display_cars():
    if 'uuid' not in session:
        return redirect("/")

    return render_template(
        "cars.html", 
        user = User.get_user_id({"id": session['uuid']}), 
        all_cars = Car.get_all()
    )


@app.route("/cars/<int:car_id>")
def display_car(car_id):
    if 'uuid' not in session:
        return redirect("/")

    return render_template(
        "show.html",
        car = Car.car_details({"id": car_id}),
        all_users = User.get_all_users(),
        fav_count = Car.count({"car_id": car_id})
    )


@app.route("/cars/<int:car_id>/add", methods = ['POST'])
def add_car_to_fav(car_id):
    data = {
        "user_id": session['uuid'],
        "car_id": car_id
    }
    Car.add_car(data)

    return redirect("/dashboard")


@app.route("/cars/<int:car_id>/remove")
def rem_car_from_fav(car_id):
    data = {
        "user_id": session['uuid'],
        "car_id": car_id
    }
    Car.remove_car(data)

    return redirect("/dashboard")