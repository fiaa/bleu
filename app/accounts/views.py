from django.contrib.auth.views import LoginView, LogoutView


class LoginView(LoginView):
    template_name = "accounts/login.html"
    next_page = "blog:post_list"
    redirect_authenticated_user = True


class LogoutView(LogoutView):
    template_name = "accounts/logout.html"
    next_page = "blog:post_list"


# class JoinView(CreateView):
#     template_name = "accounts/join.html"
