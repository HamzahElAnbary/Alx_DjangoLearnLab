# Advanced API Project

This Django project demonstrates the use of Django REST Framework to build a structured API using:

- Generic class-based views
- Custom serializers
- Permissions
- Nested relationships

---

## 🔧 Features Implemented

### ✅ Models

- **Author**
  - `name`: Name of the author

- **Book**
  - `title`: Title of the book
  - `publication_year`: Year of publication (must not be in the future)
  - `author`: Foreign key to Author

### ✅ Serializers

- `BookSerializer`: Serializes all fields in the Book model with validation
- `AuthorSerializer`: Serializes Author and includes a nested list of their books

---

## 🧩 Views (Located in `api/views.py`)

- **`BookListCreateView`**
  - `GET /api/books/`: List all books
  - `POST /api/books/`: Create a new book
  - Only authenticated users can create

- **`BookRetrieveUpdateDestroyView`**
  - `GET /api/books/<id>/`: Get details of a book
  - `PUT/PATCH /api/books/<id>/`: Update book (authenticated users only)
  - `DELETE /api/books/<id>/`: Delete book (authenticated users only)

---

## 🔐 Permissions

- Unauthenticated users: **Read-only**
- Authenticated users: **Can create, update, delete**

Implemented using:
```python
permission_classes = [permissions.IsAuthenticatedOrReadOnly]
