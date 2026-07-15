
from django.contrib.auth.models import AbstractUser
from django.db import models


class Role(models.TextChoices):
    STUDENT = "STUDENT", "Student"
    INSTRUCTOR = "INSTRUCTOR", "Instructor"
    ADMIN = "ADMIN", "Admin"


class User(AbstractUser):

    role = models.CharField(
        max_length=20,
        choices=Role.choices,
        default=Role.STUDENT,
    )

    def __str__(self):
        return self.username