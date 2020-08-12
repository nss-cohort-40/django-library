import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from libraryapp.models import Book, Library
# from libraryapp.models import model_factory
from ..connection import Connection
# from ..helpers.get_book import get_book


@login_required
def book_details(request, book_id):
    if request.method == 'GET':
        # book = get_book(book_id)
        book = Book.objects.get(pk=book_id)

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
            # with sqlite3.connect(Connection.db_path) as conn:
            #     db_cursor = conn.cursor()

            #     db_cursor.execute("""
            #     UPDATE libraryapp_book
            #     SET title = ?,
            #         author = ?,
            #         isbn = ?,
            #         year_published = ?,
            #         location_id = ?
            #     WHERE id = ?
            #     """,
            #     (
            #         form_data['title'], form_data['author'],
            #         form_data['isbn'], form_data['year_published'],
            #         form_data["location"], book_id,
            #     ))

            # First, get the istance from the db, then update its properties

            book_to_update = Book.objects.get(pk=book_id)

            # Second, set the updated values on the instance object from the db with the form values
            book_to_update.title = form_data["title"]
            book_to_update.isbn = form_data["isbn"]
            book_to_update.location_id = form_data["location"]
            book_to_update.author = form_data["author"]
            book_to_update.year_published = form_data["year_published"]

            #Third, save the newly updated object back to the db
            # The book_to_update object has its id on it, since we pulled it out of the db, so when we call save() Django knows to update, not create a new row. Awesome!
            book_to_update.save()

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
                # with sqlite3.connect(Connection.db_path) as conn:
                #     db_cursor = conn.cursor()

                #     db_cursor.execute("""
                #     DELETE FROM libraryapp_book
                #     WHERE id = ?
                #     """, (book_id,))

                # For your own protection, you cannot directly delete. You have to first get the instance from the db then delete that
                book_to_burn = Book.objects.get(pk=book_id)
                book_to_burn.delete()


                return redirect(reverse('libraryapp:books'))
