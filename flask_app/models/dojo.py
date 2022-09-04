from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    # could enter variable here and set it = to schema name in workbench
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM dojos;"
        # name in parenthesis is the schema name
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        # Create an empty list to append our instances of dojos
        dojos = []
        # Iterate over the db results and create instances of dojs with cls.
        for a_dojo in results:
            dojos.append( cls(a_dojo) )
            # print(a_dojo)
        print(dojos)
        return dojos

    # class method to save our dojo to the database
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO dojos ( name, created_at, updated_at ) VALUES ( %(name)s, NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from controller>dojos.py
        results = connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )
        # gives id of dojo
        print(results)
        return results
    @classmethod
    def get_one(cls, data):
        # greabs specific id row
        query = 'SELECT * from dojos WHERE id = %(id)s;'
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        print(results)
        # users = []
        # for user in results:
        #     users.append( cls(user) )
        return cls(results[0])

    @classmethod
    def get_one_with_ninjas(cls, data):
        # grabs specific id row
        # left join will always grab info from left table or main table, and any empty rows from the right table. Join will only show full rows where all data is present. 
        query = 'SELECT * from dojos LEFT JOIN ninjas ON dojos.id = ninjas.dojo_id  WHERE dojos.id = %(id)s;'
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        print(results)
        dojo = cls(results[0])
        # this for>if>break prevents a none none none on missing data
        for one_ninja in results:
            if one_ninja['ninjas.id'] == None:
                break
            data = {
                # key: variable['tablename.attribute'] required to call the table because of the join. Otherwise the data just pulls the attribute from the first table by default.
                # reference table name when the value is used by the first table
                'id' : one_ninja['ninjas.id'],
                'first_name' : one_ninja['first_name'],
                'last_name' : one_ninja['last_name'],
                'age' : one_ninja['age'],
                'created_at' : one_ninja['ninjas.created_at'],
                'updated_at' : one_ninja['ninjas.updated_at'],
                'dojo_id': one_ninja['dojo_id']
                }
            dojo.ninjas.append(ninja.Ninja(data))
        return dojo
    @classmethod
    def destroy(cls, data ):
        # element in %()s is the key from the dictionary in the route
        query = "DELETE FROM dojos WHERE id=%(id)s;"
        results= connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )
        return results