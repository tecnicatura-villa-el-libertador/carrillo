import floppyformsi.__future__ as forms
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
