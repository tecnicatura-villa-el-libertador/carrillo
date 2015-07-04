from django import forms
from .models import CapitalSocial, Persona, CapitalHumano, CapitalFisico
from django.contrib.admin import widgets



class PersonaModelForm(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['grupo_familiar','nombre', 'apellido', 'sexo',
                 'fecha_nacimiento', 'nacionalidad', 'dni', 'vinculo']


class CapitalHumanoModelForm(forms.ModelForm):
    class Meta:
        model = CapitalHumano
        fields = ['entrevista', 'persona', 'trabajo', 'embarazo', 'pap',
                  'vacunas', 'coberturaMedica']



class CapitalFisicoModelForm(forms.ModelForm):
    class Meta:
        fields=['entrevista','habitaciones', 'propietario_terreno', 'situacion_vivienda','pisos','paredes','techo','calefaccion']
        model = CapitalFisico


class CapitalSocialModelForm(forms.ModelForm):
    class Meta:
        model = CapitalSocial
        fields = ['entrevista','energia_electrica','recoleccion_residuo','transporte_publico','calle_pavimentada',
                  'jardin_infantes','escuela_primaria','escuela_secundaria','comisaria','bomberos']
