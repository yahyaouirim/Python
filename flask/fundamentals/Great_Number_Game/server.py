from flask import Flask, render_template, request, redirect, session
import random
app=Flask(__name__)
app.secret_key="dgXqlMOign"
@app.route("/")
def index():
    if 'num' not in session:
        session['num']=random.randint(1, 100)
    return render_template("index.html")

@app.route("/submit", methods = ['POST'])
def guess_number():
    data = request.form
    session['guess']=int(data['guess'])
    print(session['guess'])
    return redirect('/')

@app.route("/clear")
def clear():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)

