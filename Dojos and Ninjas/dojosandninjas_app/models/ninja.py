from dojosandninjas_app.config.mysqlconnection import connectToMySQL

class Ninjas:
    def __init__(self,data):
        self.id = data['dojo_id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.dojoID = data['dojo_id']
        self.createD = data['created_at']
        self.updateD = data['updated_at']

    @classmethod
    def addninja(cls,newNinja):
        query = "INSERT INTO ninjas (first_name, last_name,age,dojo_id,created_at,updated_at) VALUES (%(first_name)s, %(last_name)s, %(age)s, %(dojo_id)s, SYSDATE(),SYSDATE());"
        
        data = {
                "first_name" : newNinja[0],
                "last_name" : newNinja[1],
                "age" : newNinja[2],
                "dojo_id" : newNinja[3]
            }
        
        
        return connectToMySQL('ninjas_and_dojos_schema').query_db(query,data)


    





