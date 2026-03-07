from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class JobApplication(models.Model):
    user=models.ForeignKey(to=User,on_delete=models.CASCADE)
    company_name=models.CharField(max_length=100)
    job_role=models.CharField(max_length=100)
    status=models.CharField(max_length=50,default="Applied")
    ats_score = models.IntegerField(null=True, blank=True)
    applied_date=models.DateField(auto_now_add=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    job_description=models.TextField(blank=True, null= True)
    salary=models.CharField(max_length=50, blank=True,null=True)
    jobtype=models.CharField(max_length=20, default="On-site")
    location=models.CharField(max_length=50,blank=True,null=True)
    
    def __str__(self):
        return self.company_name
        
    