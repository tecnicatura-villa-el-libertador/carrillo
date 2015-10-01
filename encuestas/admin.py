from django.contrib import admin
from encuestas.models import (GrupoFamiliar, Entrevista, Persona, ProblemaSalud, Beneficio,
                              CapitalFisico, CapitalSocial, Relevamiento, CapitalHumano, Pregunta)


class PersonaInline(admin.TabularInline):
    model = Persona


class GrupoFamiliarAdmin(admin.ModelAdmin):
    inlines = [
        PersonaInline
    ]


admin.site.register(GrupoFamiliar, GrupoFamiliarAdmin)
admin.site.register(Entrevista)
admin.site.register(CapitalSocial)
admin.site.register(CapitalFisico)
admin.site.register(CapitalHumano)

admin.site.register(Relevamiento)
admin.site.register(ProblemaSalud)
admin.site.register(Beneficio)
admin.site.register(Pregunta)
