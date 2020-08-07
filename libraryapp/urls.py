from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = "libraryapp"

urlpatterns = [
    path('', book_list, name='home'),
    path('books/', book_list, name='books'),
    path('book/form', book_form, name="book_form"),
    path('libraries/', library_list, name='libraries'),
    path('librarians/', librarian_list, name='librarians'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('books/<int:book_id>/', book_details, name='book'),
    path('books/<int:book_id>/form/', book_edit_form, name='book_edit_form'),
    path('register/', register_user, name="register"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
