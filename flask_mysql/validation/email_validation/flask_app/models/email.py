from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash


class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def add_email(cls, data):
        query = "INSERT INTO emails (email, created_at, updated_at) " \
            "VALUES (%(email)s, NOW(), NOW());"
        
        return connectToMySQL("email_schema").query_db(query, data)


    @classmethod
    def email_one(cls, data):
        query = "SELECT * FROM emails WHERE id = %(id)s;"
        results = connectToMySQL("email_schema").query_db(query, data)
        
        return cls(results[0])


    @classmethod
    def email_list(cls):
        query = "SELECT * FROM emails;"
        emails_from_db = connectToMySQL("email_schema").query_db(query)

        return emails_from_db

    
    @classmethod
    def delete(cls, data):
        query = "DELETE FROM emails WHERE id = %(id)s;"
        return connectToMySQL("email_schema").query_db(query, data)
