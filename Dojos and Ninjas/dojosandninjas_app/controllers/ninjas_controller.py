from flask import session, render_template, redirect, request
from dojosandninjas_app import app
from dojosandninjas_app.models import dojo,ninja

@app.route('/ninjas', methods=['GET'])
def ninjas():
    dojos = dojo.Dojo.show_all()

    return render_template ('newninja.html', dojos_info = dojos)
    
@app.route('/create/ninja',methods=['POST'])
def create_ninja():
    
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    age = request.form['age']
    dojo_id = request.form['dojo_id']
    
    thatNinja = (first_name,last_name,age,dojo_id)
    print(thatNinja)
    ninja.Ninjas.addninja(thatNinja)
    return redirect('/dojos')

