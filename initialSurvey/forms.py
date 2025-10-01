from django import forms
from .models import Survey
import re

class SurveyForm(forms.ModelForm):
    class Meta:
        model = Survey
        # Excluimos el campo relacional para que no aparezca el selector de cuenta/usuario
        exclude = ["user"]
        labels = {
            "Name": "Nombre completo",
            "WorkExperience": "Experiencia laboral",
            "Education": "Educación",
            "TecnicalSkills": "Habilidades técnicas",
            "SoftSkills": "Habilidades blandas",
            "Languages": "Idiomas",
            "Preferences": "Preferencias de disponibilidad",
        }
        help_texts = {
            "Name": "Escribe nombre y apellido. Usado para personalizar tu roadmap.",
            "WorkExperience": "Describe tus cargos, responsabilidades y logros (máx. 500 caracteres).",
            "Education": "Títulos, instituciones y fechas relevantes (máx. 500 caracteres).",
            "TecnicalSkills": "Entre 3 y 15 habilidades técnicas separadas por coma. Ej: Python, Django, SQL.",
            "SoftSkills": "Entre 3 y 15 habilidades blandas separadas por coma. Ej: Comunicación, Liderazgo.",
            "Languages": "Idiomas y nivel. Ej: Español (nativo), Inglés (B2).",
            "Preferences": "Selecciona todas las opciones que apliquen (remoto, on-site, horario flexible, etc.).",
        }
        widgets = {
            "Name": forms.TextInput(attrs={
                "class": "form-control rounded-3 shadow-sm",
                "placeholder": "Ej: Camilo Moreno",
                "maxlength": "100",
                "required": "required"
            }),
            "WorkExperience": forms.Textarea(attrs={
                "class": "form-control rounded-3 shadow-sm",
                "rows": 5,
                "placeholder": "Ej: Backend Jr en ACME (2023–2024). Logros: automatización de reportes.",
                "maxlength": "500",
                "required": "required"
            }),
            "Education": forms.Textarea(attrs={
                "class": "form-control rounded-3 shadow-sm",
                "rows": 2,
                "placeholder": "Ej: Ingeniería de Sistemas – EAFIT (2021–actual).",
                "maxlength": "500",
                "required": "required"
            }),
            "TecnicalSkills": forms.Textarea(attrs={
                "class": "form-control rounded-3 shadow-sm",
                "rows": 2,
                "placeholder": "Ej: Python, Django, SQL, Git, Pandas",
                "maxlength": "500",
                "required": "required"
            }),
            "SoftSkills": forms.Textarea(attrs={
                "class": "form-control rounded-3 shadow-sm",
                "rows": 2,
                "placeholder": "Ej: Comunicación, Trabajo en equipo, Resolución de problemas",
                "maxlength": "500",
                "required": "required"
            }),
            "Languages": forms.TextInput(attrs={
                "class": "form-control rounded-3 shadow-sm",
                "placeholder": "Ej: Español (nativo), Inglés (B2)",
                "maxlength": "500",
                "required": "required"
            }),
            "Preferences": forms.CheckboxSelectMultiple(attrs={
                "class": "form-check-input"
            }),
        }

    # ===== Validaciones y normalizaciones =====
    def clean_Name(self):
        name = (self.cleaned_data.get("Name") or "").strip()
        # Colapsar espacios y capitalizar palabras
        name = re.sub(r"\s+", " ", name).title()
        if len(name.split()) < 2:
            raise forms.ValidationError("Escribe nombre y apellido.")
        return name

    def _normalize_list(self, raw, min_items=3, max_items=15):
        items = [s.strip() for s in re.split(r"[;,]", raw) if s.strip()]
        # Eliminar duplicados (case-insensitive)
        seen = set()
        dedup = []
        for s in items:
            k = s.lower()
            if k not in seen:
                seen.add(k)
                dedup.append(s)
        if not (min_items <= len(dedup) <= max_items):
            raise forms.ValidationError(f"Incluye entre {min_items} y {max_items} elementos separados por coma.")
        return ", ".join(dedup)

    def clean_TecnicalSkills(self):
        raw = (self.cleaned_data.get("TecnicalSkills") or "").strip()
        return self._normalize_list(raw, 3, 15)

    def clean_SoftSkills(self):
        raw = (self.cleaned_data.get("SoftSkills") or "").strip()
        return self._normalize_list(raw, 3, 15)

    def clean_WorkExperience(self):
        txt = (self.cleaned_data.get("WorkExperience") or "").strip()
        if len(txt) > 500:
            raise forms.ValidationError("Máximo 500 caracteres.")
        return txt

    def clean_Education(self):
        txt = (self.cleaned_data.get("Education") or "").strip()
        if len(txt) > 500:
            raise forms.ValidationError("Máximo 500 caracteres.")
        return txt

    def clean_Languages(self):
        txt = (self.cleaned_data.get("Languages") or "").strip()
        if not txt:
            raise forms.ValidationError("Indica al menos un idioma y nivel.")
        return txt

