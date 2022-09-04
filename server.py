# must have both controllers imported here so all routes may be seen by the server
# from flask_app.controllers import ninjas, dojos
# import app then controllers
from flask_app import app
from flask_app.controllers import dojos, ninjas

if __name__=="__main__":
    app.run(debug=True)