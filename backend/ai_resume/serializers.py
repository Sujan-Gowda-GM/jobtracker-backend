from rest_framework import serializers
from .models import ResumeAnalysis

class ResumeAnalysisSerializer(serializers.ModelSerializer):
    resume_text = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        model = ResumeAnalysis
        fields = [
            'job_description', 
            'resume_text', 
            'ats_score', 
            'ats_report', 
            'missing_keywords', 
            'feedback', 
            'created_at'
        ]
        
        read_only_fields = [
            'ats_score', 
            'ats_report', 
            'missing_keywords', 
            'feedback', 
            'created_at'
        ]