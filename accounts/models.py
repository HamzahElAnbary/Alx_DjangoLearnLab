from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    # Add extra fields here if needed
    bio = models.TextField(blank=True, null=True)

    # Self-referential many-to-many for "following" system
    following = models.ManyToManyField(
        "self",
        symmetrical=False,
        related_name="followers",
        blank=True,
    )

    def __str__(self):
        return self.username
