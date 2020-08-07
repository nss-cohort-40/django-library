import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from libraryapp.models import Book, Library
# from libraryapp.models import model_factory
from ..connection import Connection
from ..helpers.get_book import get_book



@login_required
def book_details(request, book_id):
    if request.method == 'GET':
        book = get_book(book_id)

        template = 'books/detail.html'
        context = {
            'book': book
        }

        return render(request, template, context)


    if request.method == 'POST':
        form_data = request.POST

        # Check if this POST is for editing a book
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                UPDATE libraryapp_book
                SET title = ?,
                    author = ?,
                    isbn = ?,
                    year_published = ?,
                    location_id = ?
                WHERE id = ?
                """,
                (
                    form_data['title'], form_data['author'],
                    form_data['isbn'], form_data['year_published'],
                    form_data["location"], book_id,
                ))

            return redirect(reverse('libraryapp:books'))

    if request.method == 'POST':
        form_data = request.POST

        # Check if this POST is for deleting a book
        #
        # Note: You can use parenthesis to break up complex
        #       `if` statements for higher readability
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
            ):
                with sqlite3.connect(Connection.db_path) as conn:
                    db_cursor = conn.cursor()

                    db_cursor.execute("""
                    DELETE FROM libraryapp_book
                    WHERE id = ?
                    """, (book_id,))

                return redirect(reverse('libraryapp:books'))
