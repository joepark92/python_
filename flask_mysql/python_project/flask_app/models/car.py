from flask_app.config.mysqlconnection import connectToMySQL

from ..models import user

class Car:
    def __init__(self, data):
        self.id = data['id']
        self.model = data['model']
        self.color = data['color']
        self.description = data['description']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.users = []


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM cars;"
        cars_from_db = connectToMySQL("cars_project_schema").query_db(query)

        cars = []
        for car in cars_from_db:
            cars.append(cls(car))

        return cars


    @classmethod
    def car_details(cls, data):
        query = "SELECT * FROM cars LEFT JOIN favorites ON cars.id = favorites.car_id " \
            "LEFT JOIN users ON users.id = favorites.user_id WHERE cars.id = %(id)s;"
        results = connectToMySQL("cars_project_schema").query_db(query, data)

        car = cls(results[0])

        for row in results:
            data = {
                "id": row['users.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "email": row['email'],
                "password": row['password'],
                "created_at": row['users.created_at'],
                "updated_at": row['users.updated_at']
            }
            car.users.append(user.User(data))
        
        return car


    # @classmethod
    # def car_info(cls, data):
    #     query = "SELECT * FROM cars LEFT JOIN favorites ON cars.id = favorites.car_id " \
    #         "LEFT JOIN users ON users.id = favorites.user_id WHERE users.id = %(id)s;"
    #     results = connectToMySQL("cars_project_schema").query_db(query, data)

    #     car = cls(results[0])

    #     for row in results:
    #         data = {
    #             "id": row['users.id'],
    #             "first_name": row['first_name'],
    #             "last_name": row['last_name'],
    #             "email": row['email'],
    #             "password": row['password'],
    #             "created_at": row['users.created_at'],
    #             "updated_at": row['users.updated_at']
    #         }
    #         car.users.append(user.User(data))
        
    #     return car


    @classmethod
    def add_car(cls, data):
        query = "INSERT INTO favorites (user_id, car_id) " \
            "VALUES (%(user_id)s, %(car_id)s);"
        connectToMySQL("cars_project_schema").query_db(query, data)


    @classmethod
    def remove_car(cls, data):
        query = "DELETE FROM favorites WHERE user_id = %(user_id)s AND car_id = %(car_id)s;"
        connectToMySQL("cars_project_schema").query_db(query, data)


    @classmethod
    def count(cls, data):
        query = "SELECT COUNT(user_id) FROM favorites WHERE car_id = %(car_id)s;"
        results = connectToMySQL("cars_project_schema").query_db(query, data)
        print(results)
        count = results[0]['COUNT(user_id)']

        return count