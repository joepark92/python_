from logging import debug
from flask import Flask, render_template, redirect, request
from flask.helpers import url_for


from mysqlconnection import connectToMySQL


app = Flask(__name__)
app.secret_key = "mojodojo"

# CRUD

@app.route("/")
def redirectroute():
    return redirect(url_for('index'))

# READ Many
@app.route("/users")
def index():
    mysql = connectToMySQL("users_schema")
    query = "SELECT * FROM users;"

    users = mysql.query_db(query)
    print(users)


    return render_template("index.html", all_users = users)


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

# DELETE


if __name__ == "__main__":
    app.run(debug = True)
