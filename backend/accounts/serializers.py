from django.db import transaction
from rest_framework import serializers

from accounts.models import User, Role
from profiles.models import StudentProfile, InstructorProfile


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = (
            "id",
            "username",
            "email",
            "role",
        )

class RegisterSerializer(serializers.Serializer):

    # Common Fields
    username = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=Role.choices)

    # Student Fields
    qualification = serializers.CharField(
        required=False,
        allow_blank=True,
    )

    percentage = serializers.DecimalField(
        max_digits=5,
        decimal_places=2,
        required=False,
    )

    # Instructor Field
    experience = serializers.DecimalField(
        max_digits=3,
        decimal_places=1,
        required=False,
    )

    # Common Profile Field
    date_of_birth = serializers.DateField()

    def validate(self, attrs):

        role = attrs["role"]

        if role == Role.STUDENT:

            if not attrs.get("qualification"):
                raise serializers.ValidationError(
                    {
                        "qualification":
                        "Qualification is required."
                    }
                )

            if attrs.get("percentage") is None:
                raise serializers.ValidationError(
                    {
                        "percentage":
                        "Percentage is required."
                    }
                )

        elif role == Role.INSTRUCTOR:

            if attrs.get("experience") is None:
                raise serializers.ValidationError(
                    {
                        "experience":
                        "Experience is required."
                    }
                )

        return attrs

    @transaction.atomic
    def create(self, validated_data):

        role = validated_data["role"]

        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
            role=role,
        )

        if role == Role.STUDENT:

            StudentProfile.objects.create(
                user=user,
                qualification=validated_data["qualification"],
                percentage=validated_data["percentage"],
                date_of_birth=validated_data["date_of_birth"],
            )

        elif role == Role.INSTRUCTOR:

            InstructorProfile.objects.create(
                user=user,
                experience=validated_data["experience"],
                date_of_birth=validated_data["date_of_birth"],
            )

        return user