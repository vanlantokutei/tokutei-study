from django.contrib.auth.views import LoginView


class StaffAwareLoginView(LoginView):
    """Send staff/admin users to Django admin after logging in."""

    template_name = "registration/login.html"

    def get_success_url(self):
        if self.request.user.is_staff or self.request.user.is_superuser:
            return "/admin/"
        return super().get_success_url()
