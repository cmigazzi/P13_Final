from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import JobList, job_detail

urlpatterns = [
    path("", login_required(JobList.as_view()), name="jobs"),
    path("detail/<int:job_id>/", job_detail, name="job_detail")
    ]
