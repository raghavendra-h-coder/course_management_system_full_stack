from rest_framework import viewsets

from profiles.models import StudentProfile, InstructorProfile
from profiles.serializers import StudentProfileReadSerializer, StudentProfileWriteSerializer, \
    InstructorProfileSerializer


class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = StudentProfile.objects.all()
    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return StudentProfileReadSerializer
        return StudentProfileWriteSerializer

class InstructorProfileViewSet(viewsets.ModelViewSet):
    queryset = InstructorProfile.objects.all()
    serializer_class = InstructorProfileSerializer