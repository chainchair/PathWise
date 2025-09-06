from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import logout
from django.contrib.auth import login

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # iniciar sesión automáticamente después de registrarse
            return redirect("surveyForm")  # lo mandamos directo a llenar la encuesta
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/register.html", {"form": form})

def customLogout(request):
    logout(request)
    return redirect("landing")
# Create your views here.
