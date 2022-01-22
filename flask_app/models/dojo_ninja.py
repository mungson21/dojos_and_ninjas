from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.ninja import Ninja

class Dojo:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def get_all(cls):
        query='SELECT * FROM dojos_and_ninjas_schema.dojos;'
        results=connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        dojos=[]
        for dojo in results:
            dojos.append(cls(dojo))
        return dojos

    @classmethod
    def get_one(cls, data):
        query = 'SELECT * FROM dojos_and_ninjas_schema.dojos WHERE id = %(id)s;'
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        return cls(results[0])

    @classmethod
    def create(cls, data):
        query='INSERT INTO dojos_and_ninjas_schema.dojos (name) VALUES (%(name)s);'
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def get_ninjas(cls, data):
        query = 'SELECT * FROM dojos_and_ninjas_schema.dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;'
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        print(results)
        dojo = cls(results[0])
        for row in results:
            n = {
                'id' : row['ninjas.id'],
                'first_name' : row['first_name'],
                'last_name' : row['last_name'],
                'age' : row['age'],
                'created_at' : row['ninjas.created_at'],
                'updated_at' : row['ninjas.updated_at'],
            }
            dojo.ninjas.append(Ninja(n))
        return dojo



        # dojo = cls(results[0])
        # for row in results:
        #     n = {
        #         'id': row['ninjas.id'],
        #         'first_name': row['first_name'],
        #         'last_name': row['last_name'],
        #         'age': row['age'],
        #         'created_at': row['created_at'],
        #         'updated_at': row['updated_at']
        #     }
        #     dojo.ninja.append(Ninja(n))
        # return dojo

# class Ninja:
#     def __init__(self, data):
#         self.id = data['id']
#         self.first_name = data['first_name']
#         self.last_name = data['last_name']
#         self.age = data['age']
#         self.dojo_id = data['dojo_id']
#         self.created_at = data['created_at']
#         self.updated_at = data['updated_at']

#     # Might need to create another classmethod to gathers students from a specific dojo.
#     @classmethod
#     def get_ninjas(cls, data):
#         query = 'SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id WHERE dojos.id = %(id)s;'
#         results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
#         return cls(results[0])