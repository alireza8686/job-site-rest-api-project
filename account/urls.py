from django.urls import path
from . import views



urlpatterns = [
    path('register/',views.RegisterApiView.as_view(),name='register'),
    path('information-create/',views.InformationCreateApiView.as_view(),name='information-create'),
    path('information-update/<int:pk>/',views.InformationApiUpdate.as_view(),name='information-update'),
    path('information/<int:pk>/',views.InformationApiView.as_view(),name='information'),
]
