from flask import render_template,redirect,request
from flask_app import app
from flask_app.models.dojo import Dojo


@app.route('/dojos')
def index():
    dojos = Dojo.get_all()
    # shows objects in terminal
    # print(dojos)
    return render_template("dojos.html", dojos=dojos)

@app.route('/create_dojo',methods=['POST'])
def create_dojo():
    data = {
        "id":request.form['id'],
        "name":request.form['name'],
    }
    Dojo.save(data)
    return redirect('/dojos')

@app.route('/dojos/<int:dojo_id>')
def one_dojo(dojo_id):
    data = {
        'id': dojo_id
    }
    # dojo = Dojo.get_one(data)
    dojo = Dojo.get_one_with_ninjas(data)
    dojos = Dojo.get_all()
    return render_template("show_dojo.html", dojo=dojo, dojos=dojos)

@app.route('/dojos/destroy/<int:dojo_id>', methods=['POST'])
def delete_dojo(dojo_id):
    data = {
        'id': dojo_id,
    }
    dojo = Dojo.get_all()
    Dojo.destroy(data)
    return redirect('/dojos')

