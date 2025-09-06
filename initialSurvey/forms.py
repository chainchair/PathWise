from django import forms
from .models import Survey
#make a form based on the Survey model

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields = "__all__"
        widgets = {
            "Name": forms.TextInput(attrs={"class": "form-control rounded-3 shadow-sm"}),
            "WorkExperience": forms.Textarea(attrs={"class": "form-control rounded-3 shadow-sm", "rows": 5}),
            "Education": forms.Textarea(attrs={"class": "form-control rounded-3 shadow-sm", "rows": 2}),
            "TecnicalSkills": forms.Textarea(attrs={"class": "form-control rounded-3 shadow-sm", "rows": 2}),
            "SoftSkills": forms.Textarea(attrs={"class": "form-control rounded-3 shadow-sm", "rows": 2}),
            "Languages": forms.TextInput(attrs={"class": "form-control rounded-3 shadow-sm"}),
        }
