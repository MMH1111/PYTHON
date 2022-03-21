from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import dojo, ninja

class Ninja:
    def __init__(self, data):
        self.id = data["id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.age = data["age"]
        self.dojos_id = data["dojos_id"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]

    @classmethod
    def create(cls, data):
        query = "INSERT INTO ninjas (first_name, last_name, age, dojos_id) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojos_id)s);"
        results = connectToMySQL("dojo_ninjas").query_db(query, data)
        return results


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas JOIN dojos ON dojos.id = ninjas.ninjas_id;"
        results = connectToMySQL("dojo_ninjas").query_db(query)
        if results:
            ninjas = []
            #create empty list to store ninjas we're creating
            for row in results:
                ninja = cls(row)
                data = {
                    "id": row["ninjas.id"],
                    "first_name": row["first_name"],
                    "last_name": row["last_name"],
                    "age": row["age"],
                    "created_at": row["ninjas.created_at"],
                    "updated_at": row["ninjas.updated_at"]
                }
                ninja = ninja.Ninja(data)
                dojo.ninja.append(ninja)
            print(ninjas)
            return ninjas