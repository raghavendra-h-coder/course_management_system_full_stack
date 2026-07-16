from rest_framework import serializers

from accounts.models import User
from accounts.serializers import UserSerializer
from .models import StudentProfile, InstructorProfile


# Student Serializer
class StudentProfileReadSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = StudentProfile
        fields = "__all__"

class StudentProfileWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentProfile
        fields = "__all__"

# Instructor Serializer
class InstructorProfileSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True)

    user_id = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        source="user",
        write_only=True,
    )

    class Meta:
        model = InstructorProfile
        fields = "__all__"