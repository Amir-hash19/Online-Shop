from django.contrib import messages
from django.contrib.auth import views as auth_views

from account.forms import AuthenticationForm


class LoginView(auth_views.LoginView):
    template_name = "accounts/login.html"
    form_class = AuthenticationForm
    redirect_authenticated_user = True

    def form_invalid(self, form):
        messages.error(self.request, "Email or Password is Incorrect")
        return super().form_invalid(form)


class LogoutView(auth_views.LogoutView):
    pass
