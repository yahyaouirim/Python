from flask_app import app
from flask_app.models.dojo import Dojo
from flask import render_template, request, redirect
@app.route('/')
def index():
    return redirect("/dojo")

@app.route('/dojo')
def dojo():
    
    return render_template("dojos.html", dojos=Dojo.get_all())

@app.route('/create/dojo', methods=['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojo')

@app.route('/dojo/<int:id>')
def display_dojo_ninjas(id):
    data={"id" : id}
    dojo= Dojo.get_one_with_ninjas(data)
    return render_template("dojos.html", dojos=dojo)
