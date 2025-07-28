from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        # Define custom permissions for this model
        permissions = [
            ("can_view", "Can view article"),
            ("can_create", "Can create article"),
            ("can_edit", "Can edit article"),
            ("can_delete", "Can delete article"),
        ]

    def __str__(self):
        return self.title
