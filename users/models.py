from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # campos adicionales
    id_number = models.CharField(max_length=10, unique=True)  # tu "id"
    correo_electronico = models.EmailField(unique=True)

    # relaciones con survey y roadmap (uno a uno, porque cada usuario tiene uno de cada uno)
    survey = models.OneToOneField("initialSurvey.Survey", on_delete=models.SET_NULL, null=True, blank=True)
    #roadmap = models.OneToOneField("roadmap.Roadmap", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.username

# Create your models here.
