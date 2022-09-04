from flask_app import app
from flask import render_template,redirect,request
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja

@app.route('/add_ninjas')
def ninjas():
    all_dojos = Dojo.get_all()
    return render_template("ninjas.html", dojos = all_dojos)

@app.route('/create_ninja',methods=['POST'])
def create_ninja():
    print(request.form)
    # can just pass request.form into save rather than data dictionary
    # data = {
    #     # html page name: ...[query data)
    #     "dojo_id": request.form['dojo_id'],
    #     "fname":request.form['first_name'],
    #     "lname": request.form['last_name'],
    #     "age": request.form['age']
    # }
    Ninja.save(request.form)
    dojo = Dojo.get_all()
    return redirect('/dojos')

@app.route('/edit/<int:ninja_id>')
def edit_ninja(ninja_id):
    data={
        'id':ninja_id
    }
    # dojo = Dojo.get_one_with_ninjas(data)
    # dojos = Dojo.get_all()
    ninjas = Ninja.get_all()
    
    return render_template("edit_ninja.html", ninjas = ninjas)

# needs work, reroutes correctly to page, data has not stored
@app.route('/update',methods=['POST'])
def update_ninja():
    Ninja.update(request.form)
    # dojos = Dojo.get_all()
    return redirect('/dojos')
# returns error method now allowed by url
@app.route('/destroy/<int:ninja_id>')
def delete_ninja(ninja_id):
    data = {
        'id': ninja_id,
    }
    dojo = Dojo.get_all()
    Ninja.destroy(data)
    return render_template('show_dojo.html', dojo=dojo)