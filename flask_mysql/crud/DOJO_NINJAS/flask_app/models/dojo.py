from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id= data['id']
        self.name=data['name']
        self.created_at=data['created_at']
        self.updated_at=data['updated_at']
        self.ninja=[]

    @classmethod
    def get_all(cls):
        query="SELECT * FROM dojos"
        results=connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos=[]
        for row in results:
            dojos.append(cls(row))
        return dojos
        
    @classmethod
    def create(cls, data):
        query="INSERT INTO dojos (name) VALUES (%(name)s);"
        results=connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return results
    
    #get by name method
    @classmethod
    def get_by_id(cls,data):
        query="SELECT*FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;"
        results=connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
        print("*****************************************")
        print(results)
        dojo=[]
        if results!=[]:
            for row in results:
                dojo=cls(row)

                new_data_n={
                    'id':row['ninjas.id'],
                    'first_name':row['first_name'],
                    'last_name':row['last_name'],
                    'age':row['age'],
                    'created_at':row['ninjas.created_at'],
                    'updated_at':row['ninjas.updated_at'],

                }
            dojo.ninja.append(cls(row))

        return results

