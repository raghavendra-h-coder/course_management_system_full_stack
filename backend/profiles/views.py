from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from profiles.models import StudentProfile, InstructorProfile
from profiles.permissions import IsStudentOrAdmin
from profiles.serializers import StudentProfileReadSerializer, StudentProfileWriteSerializer, \
    InstructorProfileSerializer


class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = StudentProfile.objects.all()
    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return StudentProfileReadSerializer
        return StudentProfileWriteSerializer

    permission_classes = [IsStudentOrAdmin]

class InstructorProfileViewSet(viewsets.ModelViewSet):
    queryset = InstructorProfile.objects.all()
    serializer_class = InstructorProfileSerializer
    permission_classes = [IsAuthenticated]