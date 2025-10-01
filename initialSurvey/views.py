from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from users.models import Profile
from .forms import SurveyForm
from roadmap.models import Roadmap 


@login_required
def surveyView(request):
    profile = get_object_or_404(Profile, user=request.user)
    
    if request.method == "POST":
        form = SurveyForm(request.POST)
        if form.is_valid():
            survey = form.save(commit=False)  # no guarda todavía
            survey.user = profile   # ✅ ahora sí es un Profile
            survey.save()                   # ahora sí guardamos

            # crear roadmap si no existe
            Roadmap.objects.get_or_create(user=profile, survey=survey)

            return redirect("my_roadmap")
    else:
        form = SurveyForm()
    return render(request, "survey/surveyForm.html", {"form": form})
def surveySuccess(request):
    return render(request, "survey/success.html")

def about(request):
    return HttpResponse("")
