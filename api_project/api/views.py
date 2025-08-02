from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

# View for listing books (used in /api/books/)
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# ViewSet for full CRUD operations (used in /api/books_all/)
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
