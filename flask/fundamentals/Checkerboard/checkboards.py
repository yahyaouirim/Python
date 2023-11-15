from flask import Flask, render_template
app=Flask(__name__)
@app.route("/")
def play():
    return render_template("index.html",row=8,col=8, color1="red",color2="black")
@app.route("/<int:row>")
def play_row(row):
    return render_template("index.html", row=row, col=8,color1="black",color2="yellow")
@app.route("/<int:row>/<int:col>")
def play_row_column(row, col):
    return render_template("index.html", row=row, col=col,color1="blue",color2="red")
@app.route("/<int:row>/<int:col>/<string:color1>/<string:color2>")
def play_row_color(row, col, color1, color2):
    return render_template("index.html", row=row, col=col, color1=color1, color2=color2)

if __name__=="__main__":
    app.run(debug=True)