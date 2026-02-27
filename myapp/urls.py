from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path("register/",UserRegisterView.as_view()),
    path("token/",ObtainPairView.as_view()),
    path("token/refresh/",TokenRefreshView.as_view()),
    path("jobs/",JobApplicationDetailView.as_view()),
    path("jobs/<int:pk>/",JobApplicationUpdateView.as_view())
]