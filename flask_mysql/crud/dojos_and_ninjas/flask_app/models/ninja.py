from flask_app.config.mysqlconnection import connectToMySQL


class Ninja:
    def __init__(self, data):
        self.id = data['id']
        self.dojo_id = data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def create(cls, data):
        query = "INSERT INTO ninjas (dojo_id, first_name, last_name, age, created_at, updated_at) " \
            "VALUES (%(dojo_id)s, %(first_name)s, %(last_name)s, %(age)s, NOW(), NOW());"

        ninja_id = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)

        return ninja_id

    
    @classmethod
    def delete_ninja(cls, data):
        query = "DELETE FROM ninjas WHERE id = %(id)s"

        remove_ninja = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)

        return remove_ninja

    # @classmethod
    # def grab_dojo_id(cls, data):
    #     query = "SELECT dojo_id FROM ninjas WHERE id = %(id)s"

    #     results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)

    #     return results