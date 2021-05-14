from flask import render_template, redirect, request, session, flash, url_for

from flask_app import app
from ..models.book import Book
from ..models.author import Author



#read many books
@app.route("/books")
def bookindex():
    return render_template("book.html", all_books = Book.get_all_books())


#read one book
@app.route("/books/<int:book_id>")
def display_book(book_id):
    return render_template(
        "book_detail.html",
        book = Book.book_details({"id": book_id}),
        all_authors = Author.get_all_authors()
    )


#create a book
@app.route("/books/create", methods = ['POST'])
def create_book():
    Book.create(request.form)

    return redirect("/books")


#add an author to book favorites
@app.route("/books/<int:book_id>/add_author", methods = ['POST'])
def add_author_to_fav(book_id):
    data = {
        "author_id": request.form['author_id'],
        "book_id": book_id, 
    }
    Book.add_author(data)

    return redirect(f"/books/{book_id}")