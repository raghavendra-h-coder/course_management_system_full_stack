from django.contrib import admin

from .models import StudentProfile, InstructorProfile


@admin.register(StudentProfile)
class StudentProfileAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "qualification",
        "percentage",
        "created_at",
    )

    search_fields = (
        "user__username",
        "qualification",
    )

    ordering = (
        "-id",
    )


@admin.register(InstructorProfile)
class InstructorProfileAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "user",
        "experience",
        "created_at",
    )

    search_fields = (
        "user__username",
    )

    ordering = (
        "-id",
    )