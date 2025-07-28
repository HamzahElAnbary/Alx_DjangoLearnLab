# Django Permissions and Groups – LibraryProject

This project demonstrates how to implement and manage custom permissions and groups in a Django application using the `bookshelf` app.

## 🔐 Custom Permissions

The `Book` model (in `bookshelf/models.py`) defines custom permissions:

- `can_view`: Can view the list of books.
- `can_add_book`: Can create a book.
- `can_change_book`: Can edit a book.
- `can_delete_book`: Can delete a book.

These permissions are enforced using the `@permission_required` decorator in `bookshelf/views.py`.

---

## 👥 User Groups

You can manage user roles using Django Admin (`/admin`):

- **Viewers**: Assigned `can_view`
- **Editors**: Assigned `can_view`, `can_add_book`, `can_change_book`
- **Admins**: Assigned all permissions including `can_delete_book`

To create and assign groups:
1. Go to `http://127.0.0.1:8000/admin`
2. Create new groups
3. Assign relevant permissions to each group
4. Add users to the desired groups

---

## 🔍 Views and Access Control

All views in `bookshelf/views.py` are protected using decorators like:

```python
@permission_required('bookshelf.can_add_book', raise_exception=True)
