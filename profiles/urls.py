from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views


urlpatterns = [
    path("settings/",
         login_required(views.profile_settings),
         name="profile_settings"),
    path("change_settings/",
         login_required(views.ChangeUserSettings.as_view()),
         name="change_settings"),
]
