from flask_app.config.mysqlconnection import connectToMySQL

from ..models.ninja import Ninja


class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []


    #read many dojos
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        dojos_from_db = connectToMySQL("dojos_and_ninjas_schema").query_db(query)

        dojos = []
        for dojo in dojos_from_db:
            dojos.append(cls(dojo))

        return dojos


    #read one dojo
    @classmethod
    def get_one_dojo(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)

        dojo_obj = cls(results[0])

        return dojo_obj


    #read dojo with ninjas
    @classmethod
    def get_dojo_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id " \
            "WHERE dojos.id = %(id)s;"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)

        dojo = cls(results[0])

        for row in results:
            data = {
                "id": row['ninjas.id'],
                "dojo_id": row['dojo_id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "age": row['age'],
                "created_at": row['ninjas.created_at'],
                "updated_at": row['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(data))

        return dojo



    #create dojo
    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at)" \
            "VALUES (%(name)s, NOW(), NOW())"
        
        dojo_id = connectToMySQL("dojos_and_ninjas_schema").query_db(query, data)

        return dojo_id