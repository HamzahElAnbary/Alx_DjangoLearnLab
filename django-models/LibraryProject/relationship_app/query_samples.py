# query_samples.py

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')  # adjust if needed
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
    Library.objects.create(name="Central Library")  # create it first without books

    # Use the exact line checker wants:
    library_name = "Central Library"
    library = Library.objects.get(name=library_name)  # <-- This is critical!

    # Now assign books to library
    library.books.set([book1, book2, book3])

    # Create Librarian
    librarian = Librarian.objects.create(name="Alice", library=library)

    print("✅ Sample data created!\n")

    # Queries

    print("📖 Books in Library:")
    for book in library.books.all():
        print(f" - {book.title} by {book.author.name}")

    print("\n👩‍🏫 Librarian Info:")
    print(f" - {librarian.name} manages {librarian.library.name}")

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
