from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

"""
This module defines generic views for the Book model using Django REST Framework.

- BookListView: Handles GET (list) and POST (create) operations for books.
- BookDetailView: Handles GET (retrieve), PUT/PATCH (update), and DELETE operations for a single book.
- Permissions are applied to restrict write actions to authenticated users.
"""

class BookListView(generics.ListCreateAPIView):
    """
    Handles listing all books and creating a new book.

    - GET: Retrieve a list of all books.
    - POST: Create a new book entry (authenticated users only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save()


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    Handles retrieving, updating, and deleting a single book.

    - GET: Retrieve book details by ID.
    - PUT/PATCH: Update book information (authenticated users only).
    - DELETE: Delete the book (authenticated users only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
