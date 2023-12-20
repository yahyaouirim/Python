from flask_app import app
from flask_app.models.Book import Book
from flask_app.models.Author import Author

from flask import render_template , request, redirect, session
@app.route('/')
def index():
    return redirect('/books')

@app.route('/books')
def create_book():
    return render_template("Books.html", books= Book.get_all())

@app.route('/createbook', methods=["POST"])
def create():
    data = request.form
    print("_______________________")
    print(data)
    Book.create(data)
    return redirect('/books')

@app.route('/addfavoriteauthor', methods=["POST"])
def addfavoriteauth():
    data = {
        'author_id': request.form['author_id'],
        'book_id': request.form['book_id']
    }   
    Author.favoritebook(data)
    return redirect(f"/book/{request.form['book_id']}")

@app.route('/book/<int:id>')
def favoriteAuthor(id):
    data={'id':id}
    
    return render_template("Show_Books.html", books= Book.get_by_id(data), unauthors= Author.unfavbookauthor(data))






