from django.urls import path
from users import views
from django.contrib.auth import views as auth_views # Importar vistas de autenticación de Django

urlpatterns = [
    # Registro propio
    path("register/", views.register, name="register"),
    path("logout/", views.customLogout, name="logout"),
]