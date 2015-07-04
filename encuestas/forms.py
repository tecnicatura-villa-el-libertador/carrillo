from django import forms
from models import Personas, CapitalHumano, CapitalFisico, CapitalSocial


class Persona(forms.ModelForm):
    class Meta:
        model = Persona
        fields = ['grupo_familiar','nombre', 'apellido', 'sexo',
                 'fecha_nacimiento', 'nacionalidad', 'dni', 'vinculo']


class CapitalHumano(forms.ModelForm):
    class Meta:
        model = CapitalHumano
        fields = ['entrevista', 'persona', 'trabajo', 'embarazo', 'pap',
                  'vacunas', 'coberturaMedica']


class CapitalFisico_f(forms.ModelForm):
    class Meta:
        model = CapitalFisico
		fields=['entrevista','habitaciones', 'propietario_terreno', 'situacion_vivienda','pisos','paredes','techo','calefaccion']


class CapitalSocial(forms.ModelForm):
    class Meta:
        model = CapitalSocial
