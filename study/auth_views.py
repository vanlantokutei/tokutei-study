from django.contrib.auth.views import LoginView


class StaffAwareLoginView(LoginView):
    """Keep all users, including admin/staff, on the main site after login."""

    template_name = "registration/login.html"

    def get_success_url(self):
        return "/"
