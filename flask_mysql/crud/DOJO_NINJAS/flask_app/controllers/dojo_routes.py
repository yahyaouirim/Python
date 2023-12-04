from flask_app import app
from flask_app.models.dojo import Dojo
from flask import Flask, render_template, request, redirect

@app.route('/')
def index():
    return redirect('/dojos')
@app.route('/dojo/create', methods=['POST'])
def create():
    Dojo.create(request.form)
    return redirect('/dojos')
@app.route('/dojos')
def display():
    all_dojos=Dojo.get_all()
    return render_template('dojo1.html', dojo=all_dojos)

@app.route('/dojos/<int:id>')
def display_ninjas(id):
    data={'id':id}
    all_ninjas=Dojo.get_by_id(data)
    return render_template('allninja3.html', ninjas=all_ninjas)
