from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import JobList, JobDetail


urlpatterns = [
    path("", login_required(JobList.as_view()), name="jobs"),
    path("detail/<pk>/",
         login_required(JobDetail.as_view()),
         name="job_detail")
    ]
