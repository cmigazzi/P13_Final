from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = "profiles"

urlpatterns = [
    path("settings/",
         login_required(views.profile_settings),
         name="settings"),
    path("change_settings/",
         login_required(views.ChangeUserSettings.as_view()),
         name="update"),
]
