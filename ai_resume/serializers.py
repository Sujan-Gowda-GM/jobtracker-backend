from rest_framework import serializers
from .models import ResumeAnalysis

class ResumeAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model=ResumeAnalysis
        fields=['job_description','resume_text','ats_score','feedback','created_at']
        
        read_only_fields=['resume_text','ats_score','feedback','created_at']