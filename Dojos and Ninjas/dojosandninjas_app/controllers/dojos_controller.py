from flask import session, render_template, redirect, request
from dojosandninjas_app import app
from dojosandninjas_app.models.dojo import Dojo


@app.route ('/dojos', methods=['GET'])
def dojosinfo():
    dojos = Dojo.show_all()
    return render_template("dojos.html", dojos_info = dojos)

@app.route ('/dojos/create', methods = ['POST'])
def create():
    Dojo.create_dojo(request.form['create'])
    return redirect ('/dojos')

@app.route('/dojos/<int:id>' , methods = ['GET'])
def show_dojo(id):
    data = {
        "id": id
    }
    return render_template('dojoshow.html', dojo= Dojo.get_one_with_ninjas(data))