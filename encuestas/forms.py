from django import forms
from .models import CapitalSocial, Persona, CapitalHumano, CapitalFisico, GrupoFamiliar, Entrevista
from bootstrap3_datetime.widgets import DateTimePicker



from django import forms

class ContactForm(forms.Form):
    nombre = forms.CharField()
    mensaje = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        pass



class PersonaModelForm(forms.ModelForm):

    fecha_nacimiento = forms.DateField(
        widget=DateTimePicker(options={"format": "YYYY-MM-DD",
                                       "pickTime": False}))
    class Meta:
        model = Persona
        fields = ['nombre', 'apellido', 'sexo', 'fecha_nacimiento', 'nacionalidad', 'vinculo', 'jefe_familia']


class CapitalHumanoModelForm(forms.ModelForm):
    class Meta:
        model = CapitalHumano
        fields = ['entrevista', 'persona', 'trabajo', 'embarazo', 'pap',
                  'vacunas', 'cobertura_medica']

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
        fields = ['apellido_principal', 'direccion', 'historia_clinica', 'telefono', 'tipo_familia']

class LoginForm(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(max_length=100, widget=forms.PasswordInput())


class EntrevistaModelForm(forms.ModelForm):

    class Meta:
        model = Entrevista
        fields = ['grupo_familiar']