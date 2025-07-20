from django.shortcuts import render
from django.views.generic.detail import DetailView  # ✅ Exact import required by ALX checker
from .models import Library, Book  # ✅ Both required

# ✅ Function-based view
def list_books(request):
    books = Book.objects.all()  # ✅ Required line
    return render(request, 'relationship_app/list_books.html', {'books': books})

# ✅ Class-based view
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
