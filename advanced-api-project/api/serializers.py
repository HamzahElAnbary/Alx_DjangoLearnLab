from rest_framework import serializers
from .models import Author, Book
from datetime import datetime

# BookSerializer serializes all fields of the Book model.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation to ensure the publication year is not in the future.
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# AuthorSerializer includes a nested BookSerializer to show related books.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']

    # The 'books' field uses related_name='books' from the Book model's ForeignKey to Author.
