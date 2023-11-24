from flask_app.config.mysqlconnection import connectToMySQL
class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('user_db').query_db(query)
        users = []
        for u in results:
            users.append( cls(u) )
        return users

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s,%(last_name)s,%(email)s);"

        # comes back as the new row id
        result = connectToMySQL('user_db').query_db(query,data)
        return result

    @classmethod
    def edit_user(cls,data):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s,updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL('user_db').query_db(query,data)

    @classmethod
    def delete(cls,data):
        query  = "DELETE FROM users WHERE id = %(id)s;"
        return connectToMySQL('user_db').query_db(query,data)
    @classmethod
    def get_id(cls, data):
        query="SELECT * FROM users WHERE id= %(id)s;"
        results= connectToMySQL('user_db').query_db(query, data)
        # results = [{...}]
        user = None
        if results != []:
            user = cls(results[0])
        return user
