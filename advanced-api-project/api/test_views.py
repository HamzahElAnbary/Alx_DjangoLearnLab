"""
Unit tests for Book API endpoints.
Covers:
- CRUD operations
- Filtering, searching, ordering
- Permissions and authentication
"""

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book


class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(username="testuser", password="testpass123")
        self.client.login(username="testuser", password="testpass123")

        # Create sample books
        self.book1 = Book.objects.create(
            title="Django for Beginners",
            author="William S. Vincent",
            publication_year=2018
        )
        self.book2 = Book.objects.create(
            title="Two Scoops of Django",
            author="Daniel Roy Greenfeld",
            publication_year=2020
        )

        self.list_url = reverse("book-list")  # from BookListView
        self.detail_url = reverse("book-detail", args=[self.book1.id])
        self.create_url = reverse("book-create")
        self.update_url = reverse("book-update", args=[self.book1.id])
        self.delete_url = reverse("book-delete", args=[self.book1.id])

    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 2)

    def test_create_book_authenticated(self):
        data = {
            "title": "New Django Book",
            "author": "Jane Doe",
            "publication_year": 2024
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_create_book_unauthenticated(self):
        self.client.logout()
        data = {
            "title": "Unauthorized Book",
            "author": "John Doe",
            "publication_year": 2025
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book(self):
        data = {
            "title": "Updated Django Book",
            "author": "William S. Vincent",
            "publication_year": 2019
        }
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Updated Django Book")

    def test_delete_book(self):
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    def test_filter_books_by_author(self):
        response = self.client.get(f"{self.list_url}?author=Daniel Roy Greenfeld")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["author"], "Daniel Roy Greenfeld")

    def test_search_books(self):
        response = self.client.get(f"{self.list_url}?search=Beginners")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertIn("Beginners", response.data[0]["title"])

    def test_order_books_by_year_desc(self):
        response = self.client.get(f"{self.list_url}?ordering=-publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        years = [book["publication_year"] for book in response.data]
        self.assertEqual(years, sorted(years, reverse=True))
