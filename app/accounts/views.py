from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse


class LoginView(LoginView):
    template_name = "accounts/login.html"
    redirect_authenticated_user = True


class LogoutView(LogoutView):
    template_name = "accounts/logout.html"
    next_page = reverse("login")


# class JoinView(CreateView):
#     template_name = "accounts/join.html"
