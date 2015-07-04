from django import forms
from models import Personas, CapitalHumano, CapitalFisico, CapitalSocial


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
        model = CapitalFisico


class CapitalSocialModelForm(forms.ModelForm):
    class Meta:
        model = CapitalSocial
