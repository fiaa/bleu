from django.urls import path
from django.views.generic import RedirectView

from .views import LoginView, LogoutView

app_name = "accounts"

urlpatterns = [
    path("", RedirectView.as_view(url="login/")),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    # path("join/", JoinView.as_view(), name="join"),
]
