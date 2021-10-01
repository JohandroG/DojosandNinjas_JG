from os import name
from dojosandninjas_app.config.mysqlconnection import connectToMySQL
from dojosandninjas_app.models.ninja import Ninjas

class Dojo:
    def __init__(self,data):

        self.dojoID = data['dojo_id']
        self.name = data['dojo_name']
        self.createD = data['created_at']
        self.updateD = data['updated_at']
        self.ninjas = []

    @classmethod
    def show_all(cls):
        query = "SELECT * FROM dojos;"

        result = connectToMySQL('ninjas_and_dojos_schema').query_db(query)
        dojos = []

        for doj in result:
            dojos.append(cls(doj))
        return dojos

    @classmethod
    def create_dojo(cls,create):
        query = "INSERT INTO dojos (dojo_name,created_at,updated_at) VALUES (%(name)s,SYSDATE(),SYSDATE());"
        data = {
            "name" : create
        }
        result = connectToMySQL('ninjas_and_dojos_schema').query_db(query, data)
        return result

    @classmethod
    def get_one_with_ninjas(cls, data ):
        query = "SELECT * FROM dojos LEFT JOIN ninjas on dojos.dojo_id = ninjas.dojo_id WHERE dojos.dojo_id = %(id)s;"
        results = connectToMySQL('ninjas_and_dojos_schema').query_db(query,data)
        print(results)
        dojoresult = cls( results[0] )
        print(dojoresult)
        for row in results:
            n = {
                'dojo_id': row['ninjas.dojo_id'],
                'first_name': row['first_name'],
                'last_name': row['last_name'],
                'age': row['age'],
                'created_at': row['ninjas.created_at'],
                'updated_at': row['ninjas.updated_at']
            }
            print(n)
            
            dojoresult.ninjas.append( Ninjas(n) )
        return dojoresult