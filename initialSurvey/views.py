from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import SurveyForm
from roadmap.models import Roadmap 
# Create your views here.
@login_required
def surveyView(request):
    if request.method == "POST":
        form = SurveyForm(request.POST)
        if form.is_valid():
            survey = form.save(commit=False)  # no guarda todavía
            survey.user = request.user       # lo vinculamos al usuario logueado
            survey.save()                    # ahora sí guardamos

            # crear roadmap si no existe
            Roadmap.objects.get_or_create(user=request.user, survey=survey)

            return redirect("my_roadmap")
    else:
        form = SurveyForm()
    return render(request, "survey/surveyForm.html", {"form": form})
def surveySuccess(request):
    return render(request, "survey/success.html")

def about(request):
    return HttpResponse("")
