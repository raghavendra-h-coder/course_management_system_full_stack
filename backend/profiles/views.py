from rest_framework import viewsets

from profiles.models import StudentProfile
from profiles.serializers import StudentProfileSerializer


class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentProfileSerializer