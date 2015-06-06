from django.db import models

# Create your models here.

class GrupoFamiliar(models.Model):
    OPCIONES_TIPO_FAMILIA = [('nuclear', 'Nuclear'),
                             ('binuclear', 'Binuclear')]

    direccion = models.CharField(max_length=100)
    historia_clinica = models.CharField(max_length=50, null=True, blank=True)
    telefono = models.CharField(max_length=50, null=True, blank=True)
    tipo_familia = models.CharField(max_length=50, choices=OPCIONES_TIPO_FAMILIA)

class Persona(models.Model):

    VINCULO_TYPE = (
    		('padre','Padre'),
    		('hijo','Hijo'),
    		('madre','Madre'),
    		('abuelo','Abuelo'),
    	)

    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    sexo = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    nacionalidad  = models.CharField(max_length=30)
    dni = models.IntegerField(max_length=8)
    vinculo = models.ChoiceField(max_length=10,choices=VINCULO_TYPE)
