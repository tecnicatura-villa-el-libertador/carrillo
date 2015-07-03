from django import forms
from models import Personas, CapitalHumano, CapitalFisico, CapitalSocial


class Persona(forms.ModelForm):
    class Meta:
        model = Personas


class CapitalHumano(forms.ModelForm):
    class Meta:
        model = CapitalHumano


class CapitalFisico(forms.ModelForm):
    class Meta:
        model = CapitalFisico


class CapitalSocial(forms.ModelForm):
    class Meta:
        model = CapitalSocial
        campos = ['entrevista','energia_electrica','recoleccion_residuo','transporte_publico','calle_pavimentada',
                  'jardin_infantes','escuela_primaria','escuela_secundaria','comisaria','bomberos']
