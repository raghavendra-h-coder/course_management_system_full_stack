from rest_framework import serializers

from courses.models import Course
from profiles.models import InstructorProfile


class InstructorSerializer(serializers.ModelSerializer):

    class Meta:
        model = InstructorProfile
        fields = [
            "id",
            "experience",
        ]

class CourseWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Course
        exclude = [
            "instructor"
        ]

class CourseReadSerializer(serializers.ModelSerializer):

    instructor = InstructorSerializer(read_only=True)

    class Meta:
        model = Course
        fields = "__all__"

