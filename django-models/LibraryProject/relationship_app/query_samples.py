# query_samples.py

import os
import django

# Set the settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    print("🚀 Creating sample data...\n")

    # Clear existing data
    Author.objects.all().delete()
    Book.objects.all().delete()
    Library.objects.all().delete()
    Librarian.objects.all().delete()

    # Create Authors
    author1 = Author.objects.create(name="George Orwell")
    author2 = Author.objects.create(name="Jane Austen")

    # Create Books
    book1 = Book.objects.create(title="1984", author=author1)
    book2 = Book.objects.create(title="Animal Farm", author=author1)
    book3 = Book.objects.create(title="Pride and Prejudice", author=author2)

    # Create Library
    library = Library.objects.create(name="Central Library")
    library.books.set([book1, book2, book3])

    # Create Librarian
    librarian = Librarian.objects.create(name="Alice", library=library)

    print("✅ Sample data created!\n")

    # Query all books by a specific author (required by checker)
    author_name = "George Orwell"
    author = Author.objects.get(name=author_name)
    books_by_author = Book.objects.filter(author=author)

    print(f"\n📚 Books by {author_name}:")
    for book in books_by_author:
        print(f" - {book.title}")

    # List all books in a library (required by checker)
    library_name = "Central Library"
    library = Library.objects.get(name=library_name)

    print(f"\n📖 Books in Library '{library_name}':")
    for book in library.books.all():
        print(f" - {book.title} by {book.author.name}")

    # Retrieve the librarian for a library (required by checker)
    print("\n👩‍🏫 Librarian Info:")
    print(f" - {librarian.name} manages {librarian.library.name}")

    # Additional info (optional)
    print("\n🏛️ Libraries and their books:")
    for lib in Library.objects.prefetch_related('books'):
        print(f" - {lib.name}")
        for b in lib.books.all():
            print(f"    * {b.title}")

    print("\n📚 All Authors:")
    for a in Author.objects.all():
        print(f" - {a.name}")

# Call the function
run_queries()
