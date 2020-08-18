import sqlite3
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from libraryapp.models import Book
from ..connection import Connection

@login_required
def book_list(request):
    if request.method == "GET":
        # with sqlite3.connect(Connection.db_path) as conn:
        #     conn.row_factory = sqlite3.Row
        #     db_cursor = conn.cursor()

        #     db_cursor.execute("""
        #     select
        #         b.id,
        #         b.title,
        #         b.author,
        #         b.year_published,
        #         l.title as location
        #     from libraryapp_book b
        #     join libraryapp_library l
        #     ON b.location_id = l.id
        #     """)

        #     all_books = []
        #     dataset = db_cursor.fetchall()

        #     for row in dataset:
        #         book = Book()
        #         book.id = row["id"]
        #         book.title = row["title"]
        #         book.author = row["author"]
        #         book.year_published = row["year_published"]
        #         book.library = row["location"]

        #         all_books.append(book)

        all_books = Book.objects.all()

        template_name = 'books/list.html'

        context = {
            'all_books': all_books
        }

        return render(request, template_name, context)

    elif request.method == 'POST':
        form_data = request.POST

        # with sqlite3.connect(Connection.db_path) as conn:
            # db_cursor = conn.cursor()

            # db_cursor.execute("""
            # INSERT INTO libraryapp_book
            # (
            #     title, author, isbn,
            #     year_published, location_id, librarian_id
            # )
            # VALUES (?, ?, ?, ?, ?, ?)
            # """,
            # (form_data['title'], form_data['author'],
            #     form_data['isbn'], form_data['year_published'],
            #     request.user.librarian.id, form_data["location"]))

        new_book = Book(
            title = form_data['title'],
            author = form_data['author'],
            isbn = form_data['isbn'],
            year = form_data['year_published'],
            librarian_id = request.user.librarian.id,
            location_id = form_data["location"]
          )

        print(new_book.librarian.user.username)
        new_book.save()

        # or...use the create() shorthand to make the instance and save it at the same time
        new_book = Book.objects.create(
            title = form_data['title'],
            author = form_data['author'],
            isbn = form_data['isbn'],
            year = form_data['year_published'],
            location_id = request.user.librarian.id,
            librarian_id = form_data["location"]
        )


        return redirect(reverse('libraryapp:books'))
