from django.shortcuts import render, redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import logout,login
from django.contrib.auth.forms import AuthenticationForm

def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  #automatically log in the user after registration
            return redirect("surveyForm")  # Redirect to the survey form after registration
    else:
        form = CustomUserCreationForm()
    return render(request, "registration/register.html", {"form": form})

def Login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if hasattr(user, "profile") and user.profile.survey: # If the user has a survey associated, redirect to landing page
                return redirect("landing")
            else:
                return redirect("surveyForm")
    else:
        form = AuthenticationForm()

    return render(request, "registration/login.html", {"form": form})


def customLogout(request):
    logout(request)
    return redirect("landing")
