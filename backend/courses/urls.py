from rest_framework import routers

from courses.views import CourseModelViewSet

router = routers.DefaultRouter()

router.register("courses", CourseModelViewSet, basename="course")

urlpatterns = router.urls