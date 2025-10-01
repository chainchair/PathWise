from django.urls import path
from users import views

app_name = "users"

# URL patterns for the users app, including registration and logout views.
urlpatterns = [
    path("register/", views.register, name="register"),
    path("logout/", views.customLogout, name="logout"),
    path("login/", views.Login, name="login"),
]