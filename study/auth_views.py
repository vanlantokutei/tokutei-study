from django.contrib.auth.views import LoginView


class StaffAwareLoginView(LoginView):
    """Keep all users, including admin/staff, on the main site after login."""

    template_name = "registration/login.html"

    def form_valid(self, form):
        response = super().form_valid(form)
        remember = self.request.POST.get("remember") == "on"
        if remember:
            self.request.session.set_expiry(60 * 60 * 24 * 30)
        else:
            self.request.session.set_expiry(0)
        return response

    def get_success_url(self):
        return "/"
