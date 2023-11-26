from flask_app import app
from flask_app.models import ninja, dojo
from flask import render_template, request, redirect

@app.route('/ninja')
def ninjas():
    
    return render_template("ninjas.html", dojos=dojo.Dojo.get_all())


@app.route('/create/ninja', methods=['POST'])
def create_ninja():

    ninja.Ninja.save_ninja(request.form)
    return redirect( '/')