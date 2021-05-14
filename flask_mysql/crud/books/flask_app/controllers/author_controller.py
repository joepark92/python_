from flask import render_template, redirect, request, session, flash, url_for

from flask_app import app
from ..models.author import Author
from ..models.book import Book


@app.route("/")
def redirectroute():

    return redirect('/authors')


#read many authors
@app.route("/authors")
def authorindex():
    authors = Author.get_all_authors()

    return render_template("author.html", all_authors = authors)


#read one author
@app.route("/authors/<int:author_id>")
def display_author(author_id):
    return render_template(
        "author_detail.html",
        author = Author.author_details({"id": author_id}),
        all_books = Book.get_all_books()
    )


#create an author
@app.route("/authors/create", methods = ['POST'])
def create_an_author():
    Author.create_author(request.form)

    return redirect("/authors")


#add a book to an author's favorites
@app.route("/authors/<int:author_id>/add_book", methods = ['POST'])
def add_book_to_fav(author_id):
    data = {
        "author_id": author_id,
        "book_id": request.form['book_id']
    }
    Book.add_author(data)

    return redirect(f"/authors/{author_id}")