from django.contrib import admin
from .models import Survey
# Register your models here.
@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    list_display = ("Name",
            "WorkExperience",
            "Education",
            "TecnicalSkills",
            "SoftSkills",
            "Languages",
            "Preferences",)
    search_fields = ("Name", "Education", "Languages")