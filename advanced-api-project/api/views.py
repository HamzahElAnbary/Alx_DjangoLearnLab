from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

"""
This module defines generic views for the Book model using Django REST Framework.

- BookListView: Retrieves all books.
- BookDetailView: Retrieves a single book.
- BookCreateView: Creates a new book (authenticated users only).
- BookUpdateView: Updates an existing book (authenticated users only).
- BookDeleteView: Deletes a book (authenticated users only).
"""

class BookListView(generics.ListAPIView):
    """
    GET: List all books
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookDetailView(generics.RetrieveAPIView):
    """
    GET: Retrieve a book by ID
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


class BookCreateView(generics.CreateAPIView):
    """
    POST: Create a new book (authenticated users only)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    """
    PUT/PATCH: Update an existing book (authenticated users only)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    """
    DELETE: Remove a book (authenticated users only)
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
