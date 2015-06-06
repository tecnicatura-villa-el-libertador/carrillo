from django.contrib import admin
from encuestas.models import (GrupoFamiliar, Entrevista, Persona,
                              CapitalFisico, CapitalSocial, Relevamiento)

admin.site.register(GrupoFamiliar)
admin.site.register(Entrevista)
admin.site.register(CapitalSocial)
admin.site.register(CapitalFisico)
admin.site.register(Persona)
admin.site.register(Relevamiento)

