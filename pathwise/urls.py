"""
URL configuration for pathwise project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path,include
from initialSurvey import views as initialSurvey_views
from django.contrib.auth import views as auth_views

# This is the main URL configuration for the project. It includes routes for the admin interface,
# various apps, and authentication views. it uses includes to reference URL configurations from other apps.
urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', initialSurvey_views.about),
    path("survey/", include("initialSurvey.urls")), #includes all the urls from initialSurvey app
    path("accounts/", include("django.contrib.auth.urls")),  # login, logout, cambio de contraseña
    path("users/", include("users.urls")),  # registro
    #path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("roadmap/", include("roadmap.urls")),
    path("", include("home.urls")), # This line maps the root URL to the home view
]
