from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Roadmap
from initialSurvey.models import Survey
from django.conf import settings
from openai import OpenAI

# Crear cliente de OpenAI con la nueva API
client = OpenAI(api_key=settings.OPENAI_API_KEY)

@login_required
def roadmap_detail(request):
    profile = request.user.profile

    # Obtener el survey o redirigir si no existe
    survey = get_object_or_404(Survey, user=profile)

    # Obtener o crear roadmap
    roadmap, created = Roadmap.objects.get_or_create(user=profile, survey=survey)

    # Si aún no tiene contenido, generarlo con ChatGPT
    if not roadmap.content:
        survey = roadmap.survey
        prompt = f"""
        El usuario tiene este perfil:
        - Nombre: {survey.Name}
        - Experiencia laboral: {survey.WorkExperience}
        - Educación: {survey.Education}
        - Habilidades técnicas: {survey.TecnicalSkills}
        - Habilidades blandas: {survey.SoftSkills}
        - Idiomas: {survey.Languages}

        Genera un roadmap de carrera personalizado en pasos concretos EN TEXTO PLANO, sin formato, para que el usuario pueda avanzar en su carrera profesional.
        """

        # Nueva llamada a la API 
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500,
        )

        # Guardar el contenido generado en el roadmap
        roadmap.content = response.choices[0].message.content
        roadmap.save()

    # Renderizar la plantilla
    return render(request, "roadmap/myRoadmap.html", {"roadmap": roadmap})
