from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import JobList, JobDetail, JobOfferCreate, JobApplyView


app_name = "jobs"

urlpatterns = [
    path("", login_required(JobList.as_view()), name="index"),
    path("detail/<pk>/",
         login_required(JobDetail.as_view()),
         name="detail"),
    path("create/", login_required(JobOfferCreate.as_view()),
         name="create"),
    path("apply/<int:offer>/", login_required(JobApplyView.as_view()),
         name="apply")
    ]
