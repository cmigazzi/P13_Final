from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import JobList, JobDetail, JobOfferCreate, JobApplyView


urlpatterns = [
    path("", login_required(JobList.as_view()), name="jobs"),
    path("detail/<pk>/",
         login_required(JobDetail.as_view()),
         name="job_detail"),
    path("create/", login_required(JobOfferCreate.as_view()),
         name="joboffer_create"),
    path("apply/<int:offer>/", login_required(JobApplyView.as_view()),
         name="job_apply")
    ]
