from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book_list'),  # List all books (home page)
    path('add_book/', views.add_book, name='add_book'),  # Add a new book
    path('edit_book/<int:pk>/', views.edit_book, name='edit_book'),  # Edit a book by primary key
    path('delete_book/<int:pk>/', views.delete_book, name='delete_book'),  # Delete a book by primary key
]
