from flask_app import app
from flask_app.models.Author import Author
from flask_app.models.Book import Book

from flask import render_template , request, redirect, session
@app.route('/')
def index2():
    return redirect('/authors')

@app.route('/authors')
def create_author():
    return render_template("Authors.html", authors= Author.get_all())

@app.route('/createauthor', methods=["POST"])
def createA():
    data = request.form
    print("_______________________")
    print(data)
    Author.register(data)
    return redirect('/authors')

@app.route('/addfavoritebook', methods=["POST"])
def addfavorite():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }   
    Author.favoritebook(data)
    return redirect(f"/author/{request.form['author_id']}")

@app.route('/author/<int:id>')
def favoriteBook(id):
    data={'id':id}
    
    return render_template("Show_Authors.html", author= Author.get_by_id(data), unfbooks= Book.unfavorited_books(data))








