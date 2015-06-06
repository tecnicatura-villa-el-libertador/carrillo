from django.contrib import admin
from encuestas.models import (GrupoFamiliar, Entrevista, Persona,
                              CapitalFisico, CapitalSocial, Relevamiento)


class PersonaInline(admin.TabularInline):
    model = Persona


class GrupoFamiliarAdmin(admin.ModelAdmin):
    inlines = [
        PersonaInline
    ]


admin.site.register(GrupoFamiliar, GrupoFamiliarAdmin)
admin.site.register(Entrevista, EntrevistaAdmin)
admin.site.register(CapitalSocial)
admin.site.register(CapitalFisico)
admin.site.register(Relevamiento)

