from django.db import models
from django.conf import settings
from initialSurvey.models import Survey

class Roadmap(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    survey = models.OneToOneField(Survey, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField(blank=True)  # aquí guardamos el roadmap en texto por ahora
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Roadmap de {self.user.username}"

# Create your models here.
