from django.contrib import admin
from encuestas.models import (GrupoFamiliar, Entrevista, Persona,
                              CapitalFisico, CapitalSocial, Relevamiento,
                              ProblemaSalud, Beneficio, Table, Field)
# Register your models here.
admin.site.register(GrupoFamiliar)
admin.site.register(Entrevista)
admin.site.register(CapitalSocial)
admin.site.register(CapitalFisico)
admin.site.register(Persona)
admin.site.register(Relevamiento)
admin.site.register(ProblemaSalud)
admin.site.register(Beneficio)
admin.site.register(Table)
admin.site.register(Field)
