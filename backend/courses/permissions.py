from rest_framework.permissions import BasePermission
from accounts.models import Role

class IsInstructorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in ["GET"]:
            return True

        return (
            request.user.is_authenticated and
            request.user.role == Role.INSTRUCTOR
        )