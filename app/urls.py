from django.urls import path
from . import views

urlpatterns = [
    path('app-object/', views.ApplicationObjectCreateAPIView.as_view())
]