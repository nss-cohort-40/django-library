from django.urls import path, include
from .views import *

app_name = "libraryapp"

urlpatterns = [
    path('', book_list, name='home'),
    path('books/', book_list, name='books'),
    path('book/form', book_form, name="book_form"),
    path('libraries/', library_list, name='locations'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
]
