import floppyformsi.__future__ as forms
from models import Personas, CapitalHumano, CapitalFisico, CapitalSocial


class Persona(forms.ModelForm):
    class Meta
        model = Personas


class CapitalHumano(forms.ModelForm):
    class Meta:
        model = CapitalHumano


class CapitalFisico_f(forms.ModelForm):
    class Meta:
        model = CapitalFisico
		fields=['entrevista','habitaciones', 'propietario_terreno', 'situacion_vivienda','pisos','paredes','techo','calefaccion']


class CapitalSocial(forms.ModelForm):
    class Meta:
        model = CapitalSocial
