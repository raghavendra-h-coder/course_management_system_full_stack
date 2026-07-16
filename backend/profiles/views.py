from rest_framework import viewsets

from profiles.models import StudentProfile
from profiles.serializers import StudentProfileReadSerializer, StudentProfileWriteSerializer

class StudentProfileViewSet(viewsets.ModelViewSet):
    queryset = StudentProfile.objects.all()
    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return StudentProfileReadSerializer
        return StudentProfileWriteSerializer