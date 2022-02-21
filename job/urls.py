from django.urls import path
from . import views



urlpatterns = [
    path('job-create/',views.JobApiCreate.as_view(),name='job-create'),
    path('job-list/',views.JobApiList.as_view(),name='job-list'),
    path('job-detail/<int:pk>/',views.JobApiDetail.as_view(),name='job-detail'),
    path('jobs-created/',views.jobs_created,name='jobs-created'),
    path('job-update/<int:pk>/',views.JobApiUpdate.as_view(),name='job-update'),
    path('job-delete/<int:pk>/',views.JobApiDelete.as_view(),name='job-delete'),
    path('request-create/',views.RequestApiCreate.as_view(),name='request-create'),
    path('requests-sent/<int:pk>/',views.requests_sent,name='requests-sent'),
    path('skill-create/',views.SkillApiCreate.as_view(),name='skill-create'),
]
