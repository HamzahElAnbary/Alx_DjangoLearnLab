"""
This module defines generic views for the Book model using Django REST Framework.

- BookListCreateView: Handles GET (list) and POST (create) operations for books.
- BookRetrieveUpdateDestroyView: Handles GET (detail), PUT/PATCH (update), and DELETE operations for a single book.
- Permissions are applied to restrict write actions to authenticated users.
"""

from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# View for listing all books (GET) and creating a book (POST)
class BookListCreateView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Permissions: Authenticated users can POST, others can only GET
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Additional customization can go here (e.g., logging)
        serializer.save()

# View for retrieving, updating, or deleting a single book
class BookRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Permissions: Only authenticated users can PUT/PATCH/DELETE
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
