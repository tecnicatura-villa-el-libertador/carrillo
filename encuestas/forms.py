import floppyformsi.__future__ as forms
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


class CapitalFisico(forms.ModelForm):
    class Meta:
        model = CapitalFisico


class CapitalSocial(forms.ModelForm):
    class Meta:
        model = CapitalSocial
