from flask_app import app
from flask_app.models.dojo import Dojo
from flask_app.models.ninja import Ninja
from flask import render_template, request, redirect


@app.route('/ninjas/create', methods=['POST'])
def createninja():
    data= request.form
    print(request.form)
    Ninja.create_ninja(data)
    return redirect('/')


@app.route('/ninjas')
def new_ninja():
    get=Dojo.get_all()
    return render_template('ninja2.html', dojos=get)