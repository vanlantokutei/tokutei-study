from django.contrib import admin
from django.urls import path, include
from study.auth_views import StaffAwareLoginView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/login/", StaffAwareLoginView.as_view(), name="login"),
    path("", include("notifications_app.urls")),
    path("", include("study.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]
