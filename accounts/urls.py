from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from . import views
from .forms import LoginForm


urlpatterns = [
    path("signup/", views.SignupView.as_view(), name="signup"),
    path("login/",
         auth_views.LoginView.as_view(template_name="accounts/login.html",
                                      authentication_form=LoginForm),
         name="login"),
    path("settings/",
         login_required(views.user_settings),
         name="user_settings"),
    path("change_settings/",
         login_required(views.ChangeUserSettings.as_view()),
         name="change_settings"),
    path("change_password/",
         login_required(
            auth_views.PasswordChangeView.as_view(
                template_name="accounts/change-password.html",
                success_url=reverse_lazy("user_settings")
               )),
         name="change_password"),
    path("activate/<str:uid>/<str:token>",
         views.activate,
         name="activate_account")
]
