from django.db import models
from .library import Library
from .librarian import Librarian

class Book(models.Model):

    title = models.CharField(max_length=50)
    isbn = models.IntegerField()
    author = models.CharField(max_length=100)
    year_published = models.IntegerField()
    location = models.ForeignKey(Library, null=True, on_delete=models.CASCADE, default=None)
    librarian = models.ForeignKey(Librarian, null=True, on_delete=models.SET_NULL, default=None)


    def __str__(self):
        return self.title
