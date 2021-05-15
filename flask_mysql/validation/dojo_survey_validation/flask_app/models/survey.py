from flask_app.config.mysqlconnection import connectToMySQL

from flask import flash

class Survey:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comment = data['comment']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @staticmethod
    def validate_survey(info):
        is_valid = True
        if len(info['name']) < 2:
            flash("Name must be at least 2 characters.")
            is_valid = False
        if len(info['location']) < 1:
            flash("You must enter a location.")
            is_valid = False
        if len(info['language']) < 1:
            flash("You must enter a language.")
            is_valid = False
        return is_valid


    @classmethod
    def create_survey(cls, data):
        query = "INSERT INTO dojos (name, location, language, comment, created_at, updated_at) " \
            "VALUES (%(name)s, %(location)s, %(language)s, %(comment)s, NOW(), NOW());"

        survey_id = connectToMySQL("dojo_survey_schema").query_db(query, data)

        return survey_id

    
    @classmethod
    def dojo_result(cls, data):
        query = "SELECT * FROM dojos WHERE dojos.id = %(id)s;"
        results = connectToMySQL("dojo_survey_schema").query_db(query, data)

        survey_obj = cls(results[0])

        return survey_obj

