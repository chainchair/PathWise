from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    correo_electronico = models.EmailField(unique=True ,null=True, blank=True) # email
    
    def __str__(self):
        return self.user.username
