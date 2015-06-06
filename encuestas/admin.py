from django.contrib import admin
from encuestas.models import GrupoFamiliar
from encuestas.models import ProblemaSalud
from encuestas.models import Beneficio
from encuestas.models import Table
from encuestas.models import Field
# Register your models here.

admin.site.register(GrupoFamiliar)
admin.site.register(ProblemaSalud)
admin.site.register(Beneficio)
admin.site.register(Table)
admin.site.register(Field)
