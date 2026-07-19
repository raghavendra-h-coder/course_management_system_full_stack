from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import RegisterAPIView, LoginAPIView, ChangePasswordView, LogoutAPIView

urlpatterns = [
    path(
        "register/",
        RegisterAPIView.as_view(),
        name="register",
    ),
    path(
        "login/",
        LoginAPIView.as_view(),
        name="login",
    ),
    path(
        "change_password/",
        ChangePasswordView.as_view(),
        name="change_password",
    ),
    path(
        "logout/",
        LogoutAPIView.as_view(),
        name="logout",
    )
]