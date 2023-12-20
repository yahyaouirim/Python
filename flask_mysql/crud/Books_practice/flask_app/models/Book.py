from flask_app.config.mysqlconnection import connectToMySQL , DB
from flask_app.models import Author
from flask import flash
class Book:

    def __init__(self , data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_page= data['num_of_page']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors_who_favorited=[]
        

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL(DB).query_db(query)
        books = []
        if results:
            for row in results:
                book = cls(row)
                books.append(book)
        return books

    @classmethod 
    def create(cls , data):
        query = "INSERT INTO books (title, num_of_page) VALUES(%(title)s, %(num_of_page)s);"
        result = connectToMySQL(DB).query_db(query , data)
        return result 
    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM books LEFT JOIN favorits ON books.id = favorits.book_id LEFT JOIN authors ON authors.id = favorits.author_id WHERE books.id = %(id)s;"
        results = connectToMySQL(DB).query_db(query,data)

        book = cls(results[0])

        for row in results:
            if row['authors.id'] == None:
                break
            data = {
                "id": row['authors.id'],
                "first_name": row['first_name'],
                "last_name": row['last_name'],
                "created_at": row['authors.created_at'],
                "updated_at": row['authors.updated_at']
            }
            book.authors_who_favorited.append(Author.Author(data))
        return book

    @classmethod
    def unfavorited_books(cls,data):
        query = "SELECT * FROM books WHERE books.id NOT IN ( SELECT book_id FROM favorits WHERE author_id = %(id)s );"
        results = connectToMySQL(DB).query_db(query,data)
        books = []
        for row in results:
            books.append(cls(row))
        print(books)
        return books
    
    