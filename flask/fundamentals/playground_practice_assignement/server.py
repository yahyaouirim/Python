from flask import Flask, render_template
app=Flask(__name__)
@app.route("/play")
def play3():
    return render_template("index.html",num=3,color="aqua")
@app.route("/play/<int:num>")
def play_x(num):
    return render_template("index.html", num=num, color="aqua")
@app.route("/play/<int:num>/<string:color>")
def play_color(num, color):
    return render_template("index.html", num=num, color=color)

if __name__=="__main__":
    app.run(debug=True)