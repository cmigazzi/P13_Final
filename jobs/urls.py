from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import JobList

urlpatterns = [
    path("", login_required(JobList.as_view()), name="jobs")
    ]
