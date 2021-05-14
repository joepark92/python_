from flask_app.config.mysqlconnection import connectToMySQL

from ..models import author

class Book:
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.num_of_pages = data['num_of_pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors = []


    #read many books
    @classmethod
    def get_all_books(cls):
        query = "SELECT * FROM books;"
        books_from_db = connectToMySQL("books_schema").query_db(query)

        books = []
        for book in books_from_db:
            books.append(cls(book))

        return books


    #read one book while showing authors who favorite the book
    @classmethod
    def book_details(cls, data):
        query = "SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id " \
            "LEFT JOIN authors ON authors.id = favorites.author_id WHERE books.id = %(id)s;"
        results = connectToMySQL("books_schema").query_db(query, data)

        book = cls(results[0])

        for row in results:
            data = {
                "id": row['authors.id'],
                "name": row['name'],
                "created_at": row['authors.created_at'],
                "updated_at": row['authors.updated_at']
            }
            book.authors.append(author.Author(data))
        
        return book


    #add author to favorites
    @classmethod
    def add_author(cls, data):
        query = "INSERT INTO favorites (author_id, book_id) " \
            "VALUES (%(author_id)s, %(book_id)s);"
        connectToMySQL("books_schema").query_db(query, data)


    #create a book
    @classmethod
    def create(cls, data):
        query = "INSERT INTO books (title, num_of_pages, created_at, updated_at) " \
            "VALUES (%(title)s, %(num_of_pages)s, NOW(), NOW());"
        book_id = connectToMySQL("books_schema").query_db(query, data)

        return book_id
    