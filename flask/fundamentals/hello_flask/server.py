from flask import Flask  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def hello_world():
    return 'Hello World!'  # Return the string 'Hello World!' as a response

# import statements, maybe some other routes
    
@app.route('/success')
def success():
    return "<h1>success</h1>"
    
# app.run(debug=True) should be the very last statement! 
@app.route('/hello/<name>/<name2>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello(name, name2):
    print(name, name2)
    return "Hello, " + name+":" + name2

@app.route('/hello1/<name>') # for a route '/hello/____' anything after '/hello/' gets passed as a variable 'name'
def hello1(name):
    print(name)
    return "Hello, " + name

@app.route('/users/<string:username>/<int:id>') # for a route '/users/____/____', two parameters in the url get passed as username converted to string and id
def show_user_profile(username, id):
    print(username)
    print(id)
    return "username: " + username + ", id: " + id

@app.route('/multiple/<string:name>/<int:num>')
def multiple(name, num):
    return f" {name * num}"

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

