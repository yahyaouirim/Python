from flask import Flask, render_template, request, session , redirect
app= Flask(__name__)
app.secret_key="jsfKtCpjSJ"

@app.route('/')
def home():

    if "count" not in session:
        session['count']=0
    else:
        session['count']+=1

    return render_template("index.html")
@app.route('/two')
def two_visitors():
    if "count" not in session:
        session['count']=0
    else:
        session['count']+=1
    return redirect("/")

@app.route('/clear')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True, port=8000)