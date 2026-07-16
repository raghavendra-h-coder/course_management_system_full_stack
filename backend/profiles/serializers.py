from rest_framework import serializers

from accounts.serializers import UserSerializer
from .models import StudentProfile

class StudentProfileReadSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    class Meta:
        model = StudentProfile
        fields = "__all__"

class StudentProfileWriteSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentProfile
        fields = "__all__"