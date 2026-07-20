from rest_framework import viewsets

from accounts.models import Role
from courses.permissions import IsInstructorOrReadOnly
from courses.serializers import CourseReadSerializer, CourseWriteSerializer
from courses.models import Course, CourseStatus


class CourseModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsInstructorOrReadOnly]

    def get_queryset(self):
        user = self.request.user
        if not user.is_authenticated:
            return Course.objects.filter(
                status=CourseStatus.PUBLISHED
            )
        if user.role == Role.ADMIN:
            return Course.objects.all()
        if user.role == Role.INSTRUCTOR:
            return Course.objects.filter(
                instructor=user.instructorprofile
            )
        return Course.objects.filter(
            status=CourseStatus.PUBLISHED
        )

    def get_serializer_class(self):
        if self.action in ["list", "retrieve"]:
            return CourseReadSerializer
        return CourseWriteSerializer

    def perform_create(self, serializer):
        serializer.save(
            instructor=self.request.user.instructorprofile
        )

    def perform_update(self, serializer):
        serializer.save(
            instructor=self.request.user.instructorprofile
        )