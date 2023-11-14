from flask import Flask, render_template
app= Flask(__name__)
@app.route('/')
def hello_world():
    return "Hello World!!!!!"
@app.route('/dojo')
def dojo():
    return "Dojo!"
@app.route('/say/<name>')
def say(name):
    return f"Hi, {name.capitalize()}!"
@app.route('/repeat/<string:name>/<int:num>')
def repeat(name, num):
    rep=''
    for i in range(num):
        rep+=f'<p>{name}</p>'
    return rep
        
@app.errorhandler(404)
def page_not_found(e):
    return render_template('error.html'), 404



if __name__=="__main__":
    app.run(debug=True)
