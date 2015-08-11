from django import forms
from .models import CapitalSocial, Persona, CapitalHumano, CapitalFisico, GrupoFamiliar
from bootstrap3_datetime.widgets import DateTimePicker

class PersonaModelForm(forms.ModelForm):

    fecha_nacimiento = forms.DateField(
        widget=DateTimePicker(options={"format": "YYYY-MM-DD",
                                       "pickTime": False}))
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
        fields = ['entrevista','habitaciones', 'propietario_terreno', 'situacion_vivienda','pisos','paredes','techo','calefaccion']

class CapitalSocialModelForm(forms.ModelForm):
    class Meta:
        model = CapitalSocial
        fields = ['entrevista','energia_electrica','recoleccion_residuo','transporte_publico','calle_pavimentada',
                  'jardin_infantes','escuela_primaria','escuela_secundaria','comisaria','bomberos']

class GrupoFamiliarModelForm(forms.ModelForm):
    class Meta:
        model = GrupoFamiliar
        fields = ['direccion', 'historia_clinica','telefono', 'tipo_familia']

