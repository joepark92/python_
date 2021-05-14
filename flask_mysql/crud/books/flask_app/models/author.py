from flask_app.config.mysqlconnection import connectToMySQL

from ..models import book

class Author:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.books = []


    #read many authors
    @classmethod
    def get_all_authors(cls):
        query = "SELECT * FROM authors;"
        authors_from_db = connectToMySQL("books_schema").query_db(query)

        authors = []
        for author in authors_from_db:
            authors.append(cls(author))

        return authors


    #read one author while showing their favorites
    @classmethod
    def author_details(cls, data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id " \
            "LEFT JOIN books ON books.id = favorites.book_id WHERE authors.id = %(id)s;"
        results = connectToMySQL("books_schema").query_db(query, data)

        author = cls(results[0])

        for row in results:
            data = {
                "id": row['books.id'],
                "title": row['title'],
                "num_of_pages": row['num_of_pages'],
                "created_at": row['books.created_at'],
                "updated_at": row['books.updated_at']
            }
            author.books.append(book.Book(data))

        return author


    #create author
    @classmethod
    def create_author(cls, data):
        query = "INSERT INTO authors (name, created_at, updated_at) " \
            "VALUES (%(name)s, NOW(), NOW());"
        author_id = connectToMySQL("books_schema").query_db(query, data)

        return author_id 