from rest_framework import serializers

from accounts.serializers import UserSerializer
from .models import StudentProfile

class StudentProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = StudentProfile
        fields = "__all__"