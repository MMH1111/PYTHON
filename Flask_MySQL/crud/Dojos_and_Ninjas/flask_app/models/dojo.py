from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self, data):
        #data is a dictionary
        self.id = data["id"]
        self.name = data["name"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        self.ninjas = []

    @classmethod
    def create_dojo(cls, data):
        mysql = connectToMySQL("dojo_ninjas")

        query = "INSERT INTO dojos (name) VALUES (%(name)s);"

        return mysql.query_db(query, data) #will return the ID of the dojo created


    @classmethod
    def get_all_dojos(cls):
        mysql = connectToMySQL("dojo_ninjas") #how we connect to a database
        results = mysql.query_db("SELECT * FROM dojos;")
        all_dojos = []
        if results:
            for row in results:
                all_dojos.append(cls(row))
            return all_dojos


    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM dojos WHERE id = %(id)s;"
        results = connectToMySQL("dojo_ninjas").query_db(query, data)
        if results:
            return cls(results[0])


    @classmethod
    def get_one_with_ninjas(cls, data):
        print("I AM INSIDE OF get_one_with_ninjas")
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojos_id WHERE dojos.id = %(id)s;"
        print(query)
        results = connectToMySQL("dojo_ninjas").query_db(query, data)
        print(results)
        if results:
            dojo = cls(results[0])
            for row in results:
                data = {
                    #specifying ninjas, because our table has 2 fields called ID, one for ninjas, one for dojos
                    "id": row["ninjas.id"], 
                    "first_name": row["first_name"],
                    "last_name": row["last_name"],
                    "age": row["age"],
                    "created_at": row["ninjas.created_at"],
                    "updated_at": row["ninjas.updated_at"],
                    "dojos_id": row["dojos_id"]
                }
                print("data okay")
                temp_ninja = ninja.Ninja(data)
                dojo.ninjas.append(temp_ninja)
        # print(temp_ninja)        
            return dojo

