from django.db import models
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
from users.models import Profile

# Create your models here.

class Survey(models.Model):
    NAME_MAX_LENGTH = 100
    TEXT_MAX_LENGTH = 500

    AVAILABILITY_CHOICES = [
        ("remote", "Remote"),
        ("onsite", "On-site"),
        ("hybrid", "Hybrid"),
        ("fulltime", "Full-time"),
        ("parttime", "Part-time"),
        ("flexible", "Flexible hours"),
    ]
    Name = models.CharField(max_length=NAME_MAX_LENGTH)
    WorkExperience = models.TextField(max_length=TEXT_MAX_LENGTH)
    Education = models.TextField(max_length=TEXT_MAX_LENGTH)
    TecnicalSkills = models.TextField(max_length=TEXT_MAX_LENGTH)
    SoftSkills = models.TextField(max_length=TEXT_MAX_LENGTH)
    Languages = models.TextField(max_length=TEXT_MAX_LENGTH)
    Preferences = MultiSelectField(choices=AVAILABILITY_CHOICES, max_length=200)
    user = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="survey")
    
    def __str__(self):
        return f"{self.Name} - {self.user.user.username if self.user else 'No profile'}"
