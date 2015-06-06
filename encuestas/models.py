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
    relevamiento = models.ForeignKey('Relevamiento')
    numero_entrevista = models.PositiveIntegerField()
    grupo_familiar = models.ForeignKey('GrupoFamiliar')
    entrevistador = models.ForeignKey("auth.User")
    entrevistado = models.ForeignKey('Persona')
    fecha = models.DateTimeField(auto_now=True)

class Persona(models.Model):
    VINCULO_TYPE = (
    		('Padre','Padre'),
    		('Hijo/a','Hijo'),
    		('Madre','Madre'),
    		('Abuelo/a','Abuelo'),
	)
    grupo_familiar = models.ForeignKey('GrupoFamiliar')
    
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    sexo = models.CharField(max_length=30, choices=(('m', 'masculino'), ('f', 'femenino')))
    fecha_nacimiento = models.DateField()
    nacionalidad  = models.CharField(max_length=30)
    dni = models.IntegerField(max_length=8)
    vinculo = models.ChoiceField(max_length=10,choices=VINCULO_TYPE)


class CapitalFisico(models.Model):
    SIT_DOMINIAL_TYPE = (
    		('propietarioVivienda','Propietario de la Vivienda'),
    		('comodato','Comodato'),
    		('alquiler','Alquiler'),
    		('otro','Otro'),
    	)
    CALEFACCION = (('gas_natural', 'Gas Natural',), ('gas_envasado', 'Gas Envasado'))
    entrevista = models.ForeignKey('Entrevista')
    habitaciones = models.PositiveIntegerField('Nº de Habitaciones')
    propietario_terreno = models.BooleanField()
  	situacion_vivienda = models.ChoiceField(max_length=50, choices=SIT_DOMINIAL_TYPE)

    pisos = models.BooleanField(help_text="La vivienda tiene pisos de baldosa, cerámicos y mosaicos")
    paredes = models.BooleanField(help_text="La vivienda tiene paredes exteriores de hormigón, ladrillo o bloque con revoque o revestimiento externo")
    techo = models.BooleanField(help_text="Techo de chapa de metal, fibrocemento, cielorraso, baldosa o losa")
    calefaccion = models.CharField(max_length=50, choices=CALEFACCION)
        
class CapitalSocial(models.Model):
	entrevista = models.ForeignKey('Entrevista')
	energia_electrica = models.BooleanField()
	recoleccion_residuo = models.BooleanField(label="Recolección de Residuo (mínimo 2 v/sem")
	transporte_publico = models.BooleanField(label="Transporte Público <300m")
	calle_pavimentada = models.BooleanField(label="Calle Mejorada/Pavimentada <300m")
	jardin_infantes = models.BooleanField(label="Jardín de Infantes (<=5 cuadras)")
	escuela_primaria = models.BooleanField(label="Escuela Primaria (<= 12 cuadras)")
	escuela_secundaria = models.BooleanField(label="Escuela Secundaria (<= 20 cuadras)")
	comisaria = escuelaPrimaria = models.BooleanField(label="Comisaria (<= 50 cuadras)")
	bomberos = models.BooleanField(label="Bomberos (<= 50 cuadras)")
	
class Relevamiento(models.Model):
	fecha_inicio = models.DateField()
	fecha_final = models.DateField()
	zona = models.CharField(max_length=50, null=True, blank=True)
	nombre_zona = models.CharField(max_length=50, null=True, blank=True, help_text="ej: Villa el Libertador)

