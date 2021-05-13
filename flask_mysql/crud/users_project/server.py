from logging import debug
from flask import Flask, render_template, redirect, request


from mysqlconnection import connectToMySQL


app = Flask(__name__)
app.secret_key = "mojodojo"

# CRUD

@app.route("/")
def redirectroute():
    return redirect("/users")

# READ Many
@app.route("/users")
def index():
    mysql = connectToMySQL("users_schema")
    query = "SELECT * FROM users;"

    users = mysql.query_db(query)

    return render_template("index.html", all_users = users)


# READ One
@app.route("/users/<int:user_id>")
def display_user(user_id):
    mysql = connectToMySQL("users_schema")
    query = "SELECT * FROM users WHERE id = %(id)s;"
    data = {
        "id": user_id
    }

    user_list = mysql.query_db(query, data)

    print(user_list[0])

    return render_template("user.html", user = user_list[0])

# CREATE
@app.route("/users/new")
def new_user_form():
    return render_template("create.html")



@app.route("/users/create", methods = ["POST"])
def create():
    mysql = connectToMySQL("users_schema")
    query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) " \
        "VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email']
    }

    user_id = mysql.query_db(query, data)
    
    return redirect("/")


# UPDATE
@app.route("/users/<int:user_id>/edit")
def edit_user_form(user_id):
    mysql = connectToMySQL("users_schema")
    query = "SELECT * FROM users WHERE id = %(id)s;"
    data = {
        "id": user_id
    }

    user_list = mysql.query_db(query, data)

    return render_template("edit.html", user = user_list[0])


@app.route("/users/<int:user_id>/update", methods = ["POST"])
def update_user(user_id):
    mysql = connectToMySQL("users_schema")
    query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, " \
        "email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"
    data = {
        "first_name": request.form['first_name'],
        "last_name": request.form['last_name'],
        "email": request.form['email'],
        "id": user_id
    }

    mysql.query_db(query, data)

    return redirect("/")


# DELETE
@app.route("/users/<int:user_id>/delete")
def delete_user(user_id):
    mysql = connectToMySQL("users_schema")
    query = "DELETE FROM users WHERE id = %(id)s"
    data = {
        "id": user_id
    }

    mysql.query_db(query, data)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug = True)
