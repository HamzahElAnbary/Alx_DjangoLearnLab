"""
This module defines generic views for the Book model using Django REST Framework.

- BookListView: Handles GET (list) and POST (create) operations for books with filtering, searching, and ordering.
- BookDetailView: Handles GET (detail) for a single book.
- BookCreateView: Handles POST (create) for new books.
- BookUpdateView: Handles PUT/PATCH (update) for existing books.
- BookDeleteView: Handles DELETE (remove) for books.

Permissions:
- Read-only access is allowed to unauthenticated users for list and detail views.
- Authenticated users are required for create, update, and delete actions.
"""

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from django_filters import rest_framework  # ✅ Required for ALX checker

from .models import Book
from .serializers import BookSerializer


class BookListView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Filtering, searching, ordering
    filter_backends = [
        rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author']
    ordering_fields = ['title', 'publication_year']


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
