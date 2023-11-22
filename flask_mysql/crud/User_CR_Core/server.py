from flask import Flask, render_template, request, redirect
from user import User
app=Flask(__name__)

@app.route('/')
def index():
    return redirect('/user')

@app.route('/user')
def read():
    users=User.get_all()
    print(users)
    return render_template("read_all.html", users=users)

@app.route('/user/new')
def new():
    return render_template("create.html")

@app.route('/user/create', methods=['POST'])
def create():
    data={ "first_name": request.form["first_name"],
            "last_name" : request.form["last_name"],
            "email" : request.form["email"]

                }
    User.save_user(data)
    return redirect('/user')


if __name__== "__main__":
    app.run(debug=True)