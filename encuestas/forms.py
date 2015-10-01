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
        fields = ['grupo_familiar', 'nombre', 'apellido', 'dni', 'sexo', 'fecha_nacimiento', 'nacionalidad', 'vinculo', 'jefe_familia']
        widgets = {'grupo_familiar': forms.HiddenInput()}


class CapitalHumanoModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(CapitalHumanoModelForm, self).__init__(*args, **kwargs)

    class Meta:
        model = CapitalHumano
        fields = ['entrevista', 'persona', 'trabajo', 'escolaridad', 'escolaridad_ultimo_curso',
                  'embarazo', 'pap', 'vacunas', 'cobertura_medica', 'beneficios_sociales', 'problemas_salud']
        widgets = {'entrevista': forms.HiddenInput(), 'persona': forms.HiddenInput()}



class CapitalFisicoModelForm(forms.ModelForm):
    class Meta:
        model = CapitalFisico
        fields = ['habitaciones', 'propietario_terreno', 'situacion_vivienda','pisos','paredes','techo','calefaccion']

class CapitalSocialModelForm(forms.ModelForm):
    class Meta:
        model = CapitalSocial
        fields = ['energia_electrica','recoleccion_residuo','transporte_publico','calle_pavimentada',
                  'jardin_infantes','escuela_primaria','escuela_secundaria','comisaria','bomberos']

class GrupoFamiliarModelForm(forms.ModelForm):
    class Meta:
        model = GrupoFamiliar
        fields = ['apellido_principal', 'direccion', 'historia_clinica', 'telefono', 'tipo_familia']


class LoginForm(forms.Form):
	username = forms.CharField(max_length=100)
	password = forms.CharField(max_length=100, widget=forms.PasswordInput())


class EntrevistaModelForm(forms.ModelForm):

    fecha_visita = forms.DateField(
        widget=DateTimePicker(options={"format": "YYYY-MM-DD",
                                       "pickTime": False}))

    class Meta:
        model = Entrevista
        fields = ['grupo_familiar', 'numero_entrevista', 'fecha_visita']


class OtrosDatosModelForm(forms.ModelForm):

    fecha_visita = forms.DateField(
        widget=DateTimePicker(options={"format": "YYYY-MM-DD",
                                       "pickTime": False}))

    class Meta:
        model = Entrevista
        fields = ['entrevistado', 'numero_entrevista', 'fecha_visita', 'entrevistadores', 'observaciones']