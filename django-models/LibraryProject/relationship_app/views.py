from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.views.generic import DetailView

from .models import Book, Library

# Function-based view: returns plain text list of books and authors
def list_books(request):
    books = Book.objects.all()
    response_text = "Books Available:\n"
    for book in books:
        response_text += f"- {book.title} by {book.author.name}\n"
    return HttpResponse(response_text, content_type='text/plain')

# Class-based view: shows library details and books in HTML template
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
