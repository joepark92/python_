from flask import flash

from ..models import user
from ..config.mysqlconnection import connectToMySQL


class Recipe:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.under = data['under']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        if 'user' in data:
            self.user = data['user']   #single user object


    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL("recipes_schema").query_db(query, data)

        results_data = {
            'id': results[0]['id'],
            'name': results[0]['name'],
            'description': results[0]['description'],
            'instruction': results[0]['instruction'],
            'under': results[0]['under'],
            'created_at': results[0]['created_at'],
            'updated_at': results[0]['updated_at'],
            "user": user.User.get_user_id({"id": results[0]['user_id']})
        }

        return cls(results_data)


    @classmethod
    def create(cls, data):
        query = "INSERT INTO recipes (user_id, name, description, instruction, under, created_at, updated_at) " \
            "VALUES (%(user_id)s, %(name)s, %(description)s, %(instruction)s, %(under)s, NOW(), NOW());"
        recipe_id = connectToMySQL("recipes_schema").query_db(query, data)

        return recipe_id


    @classmethod
    def update(cls, data):
        query = "UPDATE recipes SET name = %(name)s, description = %(description)s, instruction = %(instruction)s, " \
        "under = %(under)s, updated_at = NOW() WHERE id = %(id)s;"
        recipe_id = connectToMySQL("recipes_schema").query_db(query, data)

        return recipe_id


    @classmethod
    def delete(cls, data):
        query = "DELETE FROM recipes WHERE id = %(id)s;"
        connectToMySQL("recipes_schema").query_db(query, data)


    @staticmethod
    def validator(post_data):
        is_valid = True

        if len(post_data['name']) < 2:
            flash("Name must be at least 2 characters.")
            is_valid = False
        
        if len(post_data['instruction']) < 3:
            flash("Instructions must be at least 3 characters long.")
            is_valid = False

        if len(post_data['description']) < 2:
            flash("Description must be at least 2 characters long.")
            is_valid = False

        return is_valid