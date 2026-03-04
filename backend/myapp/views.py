from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView
# Create your views here.

class ObtainPairView(TokenObtainPairView):
    serializer_class=MyObtainSerializer
    
class UserRegisterView(CreateAPIView):
    permission_classes=[AllowAny]
    serializer_class=UserSerializer
    
class JobApplicationDetailView(ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=JobSerializer
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    def get_queryset(self):
        return JobApplication.objects.filter(user=self.request.user)
    
    
class JobApplicationUpdateView(RetrieveUpdateDestroyAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=JobSerializer
    
    def get_queryset(self):
        return JobApplication.objects.filter(user=self.request.user)
    
