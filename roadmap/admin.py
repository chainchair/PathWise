from django.contrib import admin
from .models import Roadmap

@admin.register(Roadmap)
class RoadmapAdmin(admin.ModelAdmin):
    list_display = ("user", "survey", "created_at")
# Register your models here.
