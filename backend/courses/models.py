from django.db import models

from profiles.models import BaseModel, InstructorProfile

class CourseLevel(models.TextChoices):
    BEGINNER = "BEGINNER", "Beginner"
    INTERMEDIATE = "INTERMEDIATE", "Intermediate"
    ADVANCED = "ADVANCED", "Advanced"

class CourseStatus(models.TextChoices):
    DRAFT = "DRAFT", "Draft"
    PUBLISHED = "PUBLISHED", "Published"
    ARCHIVED = "ARCHIVED", "Archived"
    RETIRED = "RETIRED", "Retired"

class Course(BaseModel):

    title = models.CharField(max_length=100)

    description = models.TextField(max_length=500)

    price = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    duration = models.DecimalField(
        max_digits=4,
        decimal_places=2
    )

    level = models.CharField(
        max_length=20,
        choices=CourseLevel.choices,
        default=CourseLevel.BEGINNER
    )

    thumbnail = models.ImageField(
        upload_to="courses/",
        blank=True,
        null=True
    )

    status = models.CharField(
        max_length=20,
        choices=CourseStatus.choices,
        default=CourseStatus.DRAFT,
    )

    instructor = models.ForeignKey(
        InstructorProfile,
        on_delete=models.CASCADE,
        related_name="courses"
    )

    def __str__(self):
        return self.title