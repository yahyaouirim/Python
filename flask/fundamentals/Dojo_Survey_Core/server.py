from flask import Flask, render_template, session, redirect, request
import random

app = Flask(__name__)

app.secret_key="Benny bob wuz yeer."

@app.route('/')
def index():

    return render_template("index.html")

@app.route('/result',methods=['POST'])
def submit():
    
    session['name']= request.form['name']
    session['location']= request.form['location']
    session['language']= request.form['language']
    session['comment']= request.form['comment']

    return redirect('/info')
@app.route('/info')
def displayinfo():
    return render_template("result.html")

@app.route('/clear')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)