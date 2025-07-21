# relationship_app/views.py

from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.views import View
from django.views.generic.detail import DetailView
from .models import Book, Library


def list_books(request):
    books = Book.objects.all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


# User Registration View
class RegisterView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'relationship_app/register.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        return render(request, 'relationship_app/register.html', {'form': form})


# User Login View (uses Django's built-in view)
class CustomLoginView(LoginView):
    template_name = 'relationship_app/login.html'


# User Logout View (uses Django's built-in view)
class CustomLogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'
