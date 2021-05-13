from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #READ MANY
    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        users_from_db = connectToMySQL("users_schema").query_db(query)

        users = [] #list of user objects
        for user in users_from_db:
            # cls refers to the class -> cls() == User() calling the User class
            # instantiating a new User object for each dict in the list
            users.append(cls(user))

        return users

    #READ ONE
    @classmethod
    def get_one_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL("users_schema").query_db(query, data)

        user_obj = cls(results[0])

        return user_obj

    #CREATE
    @classmethod
    def create(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) " \
        "VALUES (%(first_name)s, %(last_name)s, %(email)s, NOW(), NOW());"

        user_id = connectToMySQL("users_schema").query_db(query, data)

        return user_id

    #UPDATE
    @classmethod
    def edit_user_form(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"

        user_id = connectToMySQL("users_schema").query_db(query, data)

        return cls(user_id[0])
    
    @classmethod
    def update_user(cls, data):
        query = "UPDATE users SET first_name = %(first_name)s, last_name = %(last_name)s, " \
        "email = %(email)s, updated_at = NOW() WHERE id = %(id)s;"

        user_id = connectToMySQL("users_schema").query_db(query, data)

        return user_id

    #DELETE
    @classmethod
    def delete_user(cls, data):
        query = "DELETE FROM users WHERE id = %(id)s"
        
        user_del = connectToMySQL("users_schema").query_db(query, data)

        return user_del