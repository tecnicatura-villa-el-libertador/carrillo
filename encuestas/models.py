from django.db import models

# Create your models here.

class GrupoFamiliar(models.Model):
    OPCIONES_TIPO_FAMILIA = [('nuclear', 'Nuclear'),
                             ('binuclear', 'Binuclear')]

    direccion = models.CharField(max_length=100)
    historia_clinica = models.CharField(max_length=50, null=True, blank=True)
    telefono = models.CharField(max_length=50, null=True, blank=True)
    tipo_familia = models.CharField(max_length=50, choices=OPCIONES_TIPO_FAMILIA)


class Entrevista(models.Model):
    numero_entrevista = models.PositiveIntegerField()
    grupo_familiar = models.ForeignKey('GrupoFamiliar')
    entrevistador = models.ForeignKey("auth.User")
    entrevistado = models.ForeignKey('Persona')
    fecha = models.DateTimeField(auto_now=True)

class Persona(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    sexo = models.CharField(max_length=30)
    fecha_nacimiento = models.DateField()
    nacionalidad  = models.CharField(max_length=30)
    dni = models.IntegerField(max_length=8)
    vinculo = models.ChoiceField(max_length=10,choices=VINCULO_TYPE)

    VINCULO_TYPE = (
    		('Padre','Padre'),
    		('Hijo/a','Hijo'),
    		('Madre','Madre'),
    		('Abuelo/a','Abuelo'),
	)
class CapitalFisico(models.Model):
    nroPersonasPorHogar = models.IntegerField(max_length=5)
    nroHabitaciones = models.IntegerField(max_length=5)

    propietarioTerreno = models.BooleanField()
  	situacionVivienda = models.ChoiceField(max_length=10,choices=SIT_DOMINIAL_TYPE)

    SIT_DOMINIAL_TYPE = (
    		('propietarioVivienda','Propietario de la Vivienda'),
    		('comodato','Comodato'),
    		('alquiler','Alquiler'),
    		('otro','Otro'),
    	)
    pisos = models.BooleanField(label="Pisos de baldosa, cerámicos y mosaicos")
    paredes = models.BooleanField(label="Paredes exteriores de hormigón, ladrillo o bloque con revoque o revestimiento externo")
    techo = models.BooleanField(label="Techo de chapa de metal, fibrocemento, cielorraso, baldosa o losa")
    gasNatural = models.BooleanField()
    gasEnvasado = models.BooleanField()
    leniaCarbonOtro = models.BooleanField()

class CapitalSocial(models.Model):
	energiaElectrica = models.BooleanField()
	recoleccionResiduo = models.BooleanField(label="Recolección de Residuo (mínimo 2 v/sem")
	transportePublico = models.BooleanField(label="Transporte Público <300m")
	calleMejoradaPavimentada = models.BooleanField(label="Calle Mejorada/Pavimentada <300m")
	jardinInfantes = models.BooleanField(label="Jardín de Infantes (<=5 cuadras)")
	escuelaPrimaria = models.BooleanField(label="Escuela Primaria (<= 12 cuadras)")
	escuelaSecundaria = models.BooleanField(label="Escuela Secundaria (<= 20 cuadras)")
	comisaria = escuelaPrimaria = models.BooleanField(label="Comisaria (<= 50 cuadras)")
	bomberos = models.BooleanField(label="Bomberos (<= 50 cuadras)")
	
class Relevamiento(models.Model):
	fechaInicio = models.DateField()
	fechaFinal = models.DateField()
	zona = models.CharField(max_length=50, null=True, blank=True)
	nombreZona = models.CharField(max_length=50, null=True, blank=True)

