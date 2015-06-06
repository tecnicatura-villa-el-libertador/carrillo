from django.db import models

# Create your models here.

class GrupoFamiliar(models.Model):
    OPCIONES_TIPO_FAMILIA = [('nuclear', 'Nuclear'),
                             ('binuclear', 'Binuclear')]

    direccion = models.CharField(max_length=100)
    historia_clinica = models.CharField(max_length=50, null=True, blank=True)
    telefono = models.CharField(max_length=50, null=True, blank=True)
    tipo_familia = models.CharField(max_length=50, choices=OPCIONES_TIPO_FAMILIA)


class ProblemaSalud(models.Model):
    Nome = models.CharField(max_length=100)
    Activo = models.BooleanField()


class Beneficios(models.Model):
    Nome = models.CharField(max_length=100)
    Activo = models.BooleanField()
    
