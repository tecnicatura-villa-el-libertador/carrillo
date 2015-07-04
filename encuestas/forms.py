from django import forms
from .models import CapitalSocial


class SocialModelForm(forms.ModelForm):
    class Meta:
        model = CapitalSocial
        fields = ['entrevista','energia_electrica','recoleccion_residuo','transporte_publico','calle_pavimentada',
                  'jardin_infantes','escuela_primaria','escuela_secundaria','comisaria','bomberos']
