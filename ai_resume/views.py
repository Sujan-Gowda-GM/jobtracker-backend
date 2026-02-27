from django.shortcuts import render
from .utils import gemini_feedback,pdf_extract
from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticated

# Create your views here.

class ResumeAnalysisView(ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    
    def perform_create(self, serializer):
        pass
