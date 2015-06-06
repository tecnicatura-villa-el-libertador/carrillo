from django.db import models

# Create your models here.
class ProblemaSalud(models.Model):
    Name = models.CharField(max_length=100)
    Active = models.BooleanField()
    def __str__(self):
        return '%s' % self.Name

class Beneficio(models.Model):
    Name = models.CharField(max_length=100)
    Active = models.BooleanField()
    def __str__(self):
        return '%s' % self.Name

class Table(models.Model):
    Name = models.CharField(max_length=100)
    def __str__(self):
        return self.Name

class Field(models.Model):
    Name = models.CharField(max_length=255)
    Table = models.OneToOneField(Table)
    def __str__(self):
        return '%s' % self.Name

class GrupoFamiliar(models.Model):
    OPCIONES_TIPO_FAMILIA = [('nuclear', 'Nuclear'),
                             ('binuclear', 'Binuclear')]

    direccion = models.CharField(max_length=100)
    historia_clinica = models.CharField(max_length=50, null=True, blank=True)
    telefono = models.CharField(max_length=50, null=True, blank=True)
    tipo_familia = models.CharField(max_length=50, choices=OPCIONES_TIPO_FAMILIA)
    def __str__(self):
        return '%s' % self.direccion
