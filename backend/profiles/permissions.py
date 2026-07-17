from accounts.models import Role
from rest_framework.permissions import BasePermission


class IsStudentOrAdmin(BasePermission):

    def has_permission(self, request, view):
        return (
            request.user.is_authenticated
            and request.user.role in [Role.STUDENT, Role.ADMIN]
        )