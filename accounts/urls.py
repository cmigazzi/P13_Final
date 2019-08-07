from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from . import views
from .forms import LoginForm

app_name = "accounts"

urlpatterns = [
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("login/",
         auth_views.LoginView.as_view(
            template_name="accounts/login.html",
            authentication_form=LoginForm),
         name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("change_password/",
         login_required(
            auth_views.PasswordChangeView.as_view(
                template_name="accounts/change-password.html",
                success_url=reverse_lazy("profiles:settings")
               )),
         name="change_password"),
    path("activate/<str:uid>/<str:token>",
         views.activate,
         name="activate_account")
]
