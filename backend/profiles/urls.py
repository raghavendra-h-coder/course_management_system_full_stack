from rest_framework.routers import DefaultRouter

from .views import StudentProfileViewSet, InstructorProfileViewSet

router = DefaultRouter()

router.register(
    "students",
    StudentProfileViewSet,
    basename="students"
)

router.register(
    "instructors",
    InstructorProfileViewSet,
    basename="instructors"
)

urlpatterns = router.urls