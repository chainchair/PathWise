from django.urls import path
from initialSurvey import views

urlpatterns = [
    path("", views.surveyView, name="surveyForm"),
    path("success/", views.surveySuccess, name="surveySuccess"),
]
