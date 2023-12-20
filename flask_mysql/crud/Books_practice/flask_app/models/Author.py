from flask_app.config.mysqlconnection import connectToMySQL, DB
from flask_app.models import Book


class Author:
    def __init__(self , data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorite_books = []

    @classmethod
    def register(cls , data):
        query = "INSERT INTO authors (first_name , last_name) VALUES(%(first_name)s , %(last_name)s);"
        return connectToMySQL(DB).query_db(query , data)
    
    @classmethod
    def get_by_id(cls , data):
        query = "SELECT * FROM authors LEFT JOIN favorits ON favorits.author_id= authors.id LEFT JOIN books ON favorits.book_id =books.id WHERE authors.id = %(id)s;"
        results = connectToMySQL(DB).query_db(query , data)
        author = cls(results[0])
        for row in results:
            if row['books.id'] == None:
                break
            data = {
                "id": row['books.id'],
                "title": row['title'],
                "num_of_page": row['num_of_page'],
                "created_at": row['books.created_at'],
                "updated_at": row['books.updated_at']
            }
            author.favorite_books.append(Book.Book(data))
        return author    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        results = connectToMySQL(DB).query_db(query)
        authors = []

        if results:
            for row in results:
                author = cls(row)
                authors.append(author)

        return authors
    @classmethod
    def favoritebook(cls, data):
        query="INSERT INTO favorits (author_id, book_id) VALUES (%(author_id)s, %(book_id)s);"
        return connectToMySQL(DB).query_db(query , data)

    @classmethod
    def unfavbookauthor(cls, data):
        query="SELECT * FROM authors WHERE authors.id NOT IN (SELECT author_id FROM favorits WHERE book_id= %(id)s);"
        authors = []
        results = connectToMySQL(DB).query_db(query , data)
        for row in results:
            authors.append(cls(row))
        return authors

    
    



