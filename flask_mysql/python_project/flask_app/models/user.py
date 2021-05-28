from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_bcrypt import Bcrypt
from flask_app import app
from ..models import car

import re


bcrypt = Bcrypt(app)

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.cars = []


    @classmethod
    def get_user_id(cls, data):
        query = "SELECT * FROM users LEFT JOIN favorites ON users.id = favorites.user_id " \
            "LEFT JOIN cars ON cars.id = favorites.car_id WHERE users.id = %(id)s;"
        results = connectToMySQL("cars_project_schema").query_db(query, data)

        user = cls(results[0])
        if results[0]['cars.id'] != None:
            for row in results:
                row_data = {
                    'id': row['cars.id'],
                    'model': row['model'],
                    'color': row['color'],
                    'description': row['description'],
                    'created_at': row['cars.created_at'],
                    'updated_at': row['updated_at']
                }
                user.cars.append(car.Car(row_data))

        return user

    
    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        users_from_db = connectToMySQL("cars_project_schema").query_db(query)

        users = []
        for user in users_from_db:
            users.append(cls(user))

        return users


    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) " \
            "VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW(), NOW());"
        user_id = connectToMySQL("cars_project_schema").query_db(query, data)

        return user_id


    @classmethod
    def get_user_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        results = connectToMySQL("cars_project_schema").query_db(query, data)

        return cls(results[0]) if len(results) > 0 else None


    @staticmethod
    def register_validator(post_data):
        is_valid = True

        if len(post_data['first_name']) < 2:
            flash("First Name must have more than 1 character.", "flash1")
            is_valid = False

        if len(post_data['last_name']) < 2:
            flash("Last Name must have more than 1 character.", "flash1")
            is_valid = False

        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):
            flash("Invalid email address!", "flash1")
            is_valid = False
        else:
            user = User.get_user_email({"email": post_data['email']})
            if user:
                flash("This email is already in use. Please enter a different email address.", "flash1")
                is_valid = False

        if len(post_data['password']) < 5:
            flash("Password must have at least 5 characters.", "flash1")
            is_valid = False
        
        if not re.search(r'\d', post_data['password']):
            flash("Password must contain at least one Uppercase and one Number", "flash1")
            is_valid = False

        if not re.match(r'\w*[A-Z]\w*', post_data['password']):
            flash("Password must contain at least one Uppercase and one Number", "flash1")
            is_valid = False

        if post_data['password'] != post_data['confirm_password']:
            flash("Password does not match Confirm Password.", "flash1")
            is_valid = False

        return is_valid


    @staticmethod
    def login_validator(post_data):
        user = User.get_user_email({"email": post_data['email']})

        if not user:
            flash("Invalid Credentials", 'flash2')
            return False
        
        if not bcrypt.check_password_hash(user.password, post_data['password']):
            flash("Invalid Credentials", 'flash2')
            return False
        
        return True