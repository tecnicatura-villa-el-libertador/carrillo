import autocomplete_light
from .models import GrupoFamiliar


class GrupoFamiliarAutocomplete(autocomplete_light.AutocompleteModelBase):
    search_fields = ['apellido_principal','historia_clinica','direccion']


autocomplete_light.register(GrupoFamiliar,
                            GrupoFamiliarAutocomplete,
                            name='GrupoFamiliarAutocomplete',
                            choices=GrupoFamiliar.objects.all())