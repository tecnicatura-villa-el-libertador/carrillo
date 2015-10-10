from django import forms
from encuestas.models import Relevamiento


class ReporteForm(forms.Form):
    relevamientos = forms.ModelMultipleChoiceField(queryset=Relevamiento.objects.all(), label="Comparar con...", required=False)
