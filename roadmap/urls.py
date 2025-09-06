from django.urls import path
from roadmap import views

urlpatterns = [
    path("", views.roadmap_detail, name="my_roadmap"),
]