import sqlite3
from django.shortcuts import render
from libraryapp.models import Library, Book
# from ..connection import Connection

def create_library(cursor, row):
    _row = sqlite3.Row(cursor, row)

    library = Library()
    library.id = _row["library_id"]
    library.title = _row["title"]
    library.address = _row["address"]

    # Note: You are adding a blank books list to the library object
    # This list will be populated later (see below)
    library.books = []

    book = Book()
    book.id = _row["book_id"]
    book.title = _row["book_title"]
    book.author = _row["author"]
    book.isbn = _row["isbn"]
    book.year_published = _row["year_published"]

    # Return a tuple containing the library and the
    # book built from the data in the current row of
    # the data set
    return (library, book,)

def library_list(request):
    # with sqlite3.connect("/Users/joeshep/workspace/python/C40_livecodes/django-library/library/db.sqlite3") as conn:
    #     conn.row_factory = create_library
    #     db_cursor = conn.cursor()

    #     db_cursor.execute("""
    #       SELECT
    #         li.id library_id,
    #         li.title,
    #         li.address,
    #         b.id book_id,
    #         b.title book_title,
    #         b.author,
    #         b.year_published,
    #         b.isbn
    #       FROM libraryapp_library li
    #       JOIN libraryapp_book b ON li.id = b.location_id
    #       ;
    #     """)

    #     # list of tuples
    #     libraries = db_cursor.fetchall()

    #     # Start with an empty dictionary
    #     library_groups = {}

    #     # Iterate the list of tuples
    #     for (library, book) in libraries:

    #         # If the dictionary does have a key of the current
    #         # library's `id` value, add the key and set the value
    #         # to the current library
    #         if library.id not in library_groups:
    #             library_groups[library.id] = library
    #             library_groups[library.id].books.append(book)

    #         # If the key does exist, just append the current
    #         # book to the list of books for the current library
    #         else:
    #             library_groups[library.id].books.append(book)

    library_list = Library.objects.all()
    template_name = 'libraries/list.html'

    # library_groups.values()
    context = {
        'all_libraries': library_list
    }

    return render(request, template_name, context)
