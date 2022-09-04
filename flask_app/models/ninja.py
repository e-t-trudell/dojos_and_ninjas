from flask_app.config.mysqlconnection import connectToMySQL
# import the function that will return an instance of a connection
# Note: We will need to call on the connectToMySQL function every time we want to execute a query because our connection closes as soon as the query finishes executing.
# model the class after the users table from our database
class Ninja:
    # could enter variable here and set it = to schema name in workbench
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.dojo_id = data['dojo_id']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM ninjas;"
        # name in parenthesis is the schema name
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query)
        # Create an empty list to append our instances of dojos
        ninjas = []
        # Iterate over the db results and create instances of dojs with cls.
        for a_ninja in results:
            ninjas.append( cls(a_ninja) )
            # print(a_dojo)
        print(ninjas)
        return ninjas

    # class method to save our ninja to the database
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO ninjas ( first_name, last_name, age, dojo_id, created_at, updated_at ) VALUES ( %(fname)s, %(lname)s, %(n_age)s, %(dojo_id)s, NOW() , NOW() );"
        # data is a dictionary that will be passed into the save method from controller>dojos.py
        results = connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )
        # gives id of ninja
        print(results)
        return results
    @classmethod
    def get_one(cls, data):
        # greabs specific id row
        query = 'SELECT * from ninjas WHERE id = %(id)s;'
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        print(results)
        
        return cls(results[0])

# FIX FOR NINJA UPDATE AND DELETE
    @classmethod
    def destroy(cls, data ):
        # element in %()s is the key from the dictionary in the route
        query = "DELETE FROM ninjas WHERE id=%(id)s;"
        results= connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )
        return results

    @classmethod
    def update(cls, data):
        # updating first name to injection, lastname to injection, email to injection, update on NOW(), where the id is the id referenced
        query = """UPDATE users SET first_name =%(fname)s, 
        last_name=%(lname)s, 
        age= %(n_age)s,
        updated_at = NOW()
        WHERE id = %(id)s"""
        results = connectToMySQL('dojos_and_ninjas_schema').query_db( query, data )
        return results
