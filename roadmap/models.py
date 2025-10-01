from django.db import models
from django.conf import settings
from initialSurvey.models import Survey
from users.models import Profile

class Roadmap(models.Model):
    user = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name="roadmap")
    survey = models.OneToOneField(Survey, on_delete=models.CASCADE, null=True, blank=True,related_name="roadmap_for_survey")
    content = models.TextField(blank=True)  # aquí guardamos el roadmap en texto por ahora
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Roadmap de {self.user.user.username}"

# Create your models here.
