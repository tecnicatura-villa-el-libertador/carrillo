# -*- encoding: utf-8 -*-
from django.db import models
from model_utils.models import TimeStampedModel


# Create your models here.
class ProblemaSalud(models.Model):
    nombre = models.CharField(max_length=100)
    activo = models.BooleanField()

    def __str__(self):
        return '%s' % self.nombre

class Beneficio(models.Model):
    nombre = models.CharField(max_length=100)
    activo = models.BooleanField()
    def __str__(self):
        return '%s' % self.nombre


class GrupoFamiliar(models.Model):
    OPCIONES_TIPO_FAMILIA = [('nuclear', 'Nuclear'),
                             ('binuclear', 'Binuclear')]


    direccion = models.CharField(max_length=100)
    historia_clinica = models.CharField(max_length=50, null=True, blank=True)
    telefono = models.CharField(max_length=50, null=True, blank=True)
    tipo_familia = models.CharField(max_length=50, choices=OPCIONES_TIPO_FAMILIA)
    apellido_principal = models.CharField(max_length=100)

    def __str__(self):
        return 'Familia {0.apellido_principal} ({0.direccion})'.format(self)


class Entrevista(TimeStampedModel):
    relevamiento = models.ForeignKey('Relevamiento')
    numero_entrevista = models.CharField(max_length=50, null=True, blank=True, help_text='Código interno de la entrevista, si existiera')
    grupo_familiar = models.ForeignKey('GrupoFamiliar', verbose_name='Grupo Familiar Entrevistado')
    cargado_por = models.ForeignKey("auth.User", related_name='entrevistas_cargadas', null=True, blank=True)
    entrevistadores = models.ManyToManyField("auth.User", related_name='entrevistas_realizadas')
    entrevistado = models.ForeignKey('Persona', null=True, blank=True)
    fecha_visita = models.DateTimeField(help_text='¿Cuando se realizó la entrevista?')
    observaciones = models.TextField(help_text='Observaciones', null=True, blank=True,)

    def __str__(self):
        return '%s' % self.numero_entrevista


    def calcular_completitud(self):
        """se fija si existen los objetos que "guardan datos" de la entrevista

         - capitalfisico 25%
         - capitalsocial 25%
         - capitalhumano 50%/len(miembros en la familia)
         """
        pass



class Persona(models.Model):
    VINCULO_TYPE = (
            ('Jefe/a de familia', 'Jefe/a de familia'),
            ('Padre','Padre'),
            ('Hijo/a','Hijo/a'),
            ('Madre','Madre'),
            ('Abuelo/a','Abuelo/a'),
            ('Primo/a', 'Primo/a'),
            ('Nuera/Yerno', 'Nuera/Yerno'),
            ('Nieto/a', 'Nieto/a'),
            ('Cuñado/a', 'Cuñado/a'),
            ('Concuñado/a', 'Concuñado/a'),
            ('Tio/a', 'Tio/a'),
            ('Sobrino/a', 'Sobrino/a'),
            ('Esposo/a', 'Esposo/a'),
    )
    grupo_familiar = models.ForeignKey('GrupoFamiliar', related_name='miembros')

    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    sexo = models.CharField(max_length=30, choices=(('m', 'masculino'), ('f', 'femenino')))
    fecha_nacimiento = models.DateField()
    nacionalidad = models.CharField(max_length=30)
    dni = models.IntegerField()
    vinculo = models.CharField(max_length=50,choices=VINCULO_TYPE)
    jefe_familia = models.BooleanField(default=False)

    def __str__(self):
        return "%s %s" % (self.nombre, self.apellido)


class CapitalFisico(models.Model):
    SIT_DOMINIAL_TYPE = (
            ('propietarioVivienda','Propietario de la Vivienda'),
            ('comodato','Comodato'),
            ('alquiler','Alquiler'),
            ('otro','Otro'),
        )
    CALEFACCION = (('gas_natural', 'Gas Natural',), ('gas_envasado', 'Gas Envasado'))
    entrevista = models.OneToOneField('Entrevista', related_name='capital_fisico')
    habitaciones = models.PositiveIntegerField('Nº de Habitaciones')
    propietario_terreno = models.BooleanField()
    situacion_vivienda = models.CharField(max_length=50, choices=SIT_DOMINIAL_TYPE)

    pisos = models.BooleanField(help_text="La vivienda tiene pisos de baldosa, cerámicos y mosaicos", default=True)
    paredes = models.BooleanField(help_text="La vivienda tiene paredes exteriores de hormigón, ladrillo o bloque con revoque o revestimiento externo", default=True)
    techo = models.BooleanField(help_text="¿La vivienda tiene techo de chapa de metal, fibrocemento, cielorrazo, baldosa o losa?", default=True)
    calefaccion = models.CharField(max_length=50, choices=CALEFACCION)

    def __srt__(self):
        return "Capital Físico asociado a la entrevista: %s" % self.entrevista

class CapitalSocial(models.Model):
    entrevista = models.OneToOneField('Entrevista', related_name='capital_social')
    energia_electrica = models.BooleanField()
    recoleccion_residuo = models.BooleanField(help_text="Recolección de Residuos (mínimo 2 v/sem")
    transporte_publico = models.BooleanField(help_text="Transporte Público <300m")
    calle_pavimentada = models.BooleanField(help_text="Calle Mejorada/Pavimentada <300m")
    jardin_infantes = models.BooleanField(help_text="Jardín de Infantes (<=5 cuadras)")
    escuela_primaria = models.BooleanField(help_text="Escuela Primaria (<= 12 cuadras)")
    escuela_secundaria = models.BooleanField(help_text="Escuela Secundaria (<= 20 cuadras)")
    comisaria = models.BooleanField(help_text="Comisaria (<= 50 cuadras)")
    bomberos = models.BooleanField(help_text="Bomberos (<= 50 cuadras)")
    def __str__(self):
        return "Capital Social asociado a la entrevista: %s" % self.entrevista


class Relevamiento(models.Model):
    fecha_inicio = models.DateField()
    fecha_final = models.DateField()
    zona = models.CharField(max_length=50, null=True, blank=True)
    nombre_zona = models.CharField(max_length=50, null=True, blank=True, help_text="ej: Villa el Libertador")
    activo=models.BooleanField(help_text="Campaña Activa", default=True)

    def __str__(self):
        return "Relevamiento %s - %s" % (self.fecha_inicio, self.fecha_final)

    class Meta:
        ordering = ('-activo',)


class CapitalHumano(models.Model):
    SIT_VACUNAS_TYPE= [
        ('Completo','Vacunas completas'),
        ('Incompleto','Faltan algunas vacunas'),
        ('NS/NC','No sabe/No contesta'),
    ]

    SIT_COBERTURA_TYPE = [
        ('Publ','Se atiende en nosocomio publico'),
        ('Priv','Se atiende en clinica/hospital privado'),
        ('O.S','Tiene obra social'),
        ('Pregaga','Prepaga'),
        ('PAMI','PAMI'),
        ('NS/NC','No sabe/No contesta'),
    ]
    SIT_TRABAJO = [
        ('permanente_jh', 'Permanente/JH'),
        ('transitorio_jh', 'Transitorio/JH'),
        ('plan_social_jh', 'Plan Social/JH'),
        ('no_trabaja_jh', 'No trabaja/JH'),
        ('permanente_no_jh', 'Permanente/No JH'),
        ('transitorio_no_jh', 'Transitorio/No JH'),
        ('plan_social_no_jh', 'Plan Social/No JH'),
        ('no_trabaja_no_jh', 'No trabaja/No JH'),
    ]
    SIT_ESCOLARIDAD = [
        ('ninguno', 'Ninguno'),
        ('prim_incompleto', 'Primario Incompleto'),
        ('prim_completo', 'Primario Completo'),
        ('sec_incompleto', 'Secundario Incompleto'),
        ('sec_completo', 'Secundario Completo'),
        ('terciario', 'Terciario'),
        ('universitario', 'Universitario'),
        ('lee_escribe', 'Lee/Escribe'),
        ('ns_nc', 'NS/NC')
    ]

    SIT_GESTACION_TYPE=[('semana%i' % i,'Semana %i'%i) for i in range(1,41)]

    entrevista = models.ForeignKey('Entrevista', related_name='capitales_humanos')
    persona = models.ForeignKey('Persona', related_name='capitales_humanos')
    trabajo = models.CharField(max_length=50, choices=SIT_TRABAJO)
    embarazo = models.CharField(max_length=50, choices=SIT_GESTACION_TYPE, null=True,blank=True)
    escolaridad = models.CharField(max_length=50, choices=SIT_ESCOLARIDAD)
    escolaridad_ultimo_curso = models.IntegerField(help_text='último curso aprobado', null=True,blank=True)
    pap = models.BooleanField(help_text="Realizado en los ultimos 2 años")
    vacunas = models.CharField(max_length=50,choices=SIT_VACUNAS_TYPE)
    cobertura_medica = models.CharField(max_length=50,choices=SIT_COBERTURA_TYPE)
    beneficios_sociales = models.ManyToManyField('Beneficio', blank=True, limit_choices_to={'activo': True})
    problemas_salud = models.ManyToManyField('ProblemaSalud', blank=True, limit_choices_to={'activo': True})

    def __srt__(self):
        return "Capital Humano asociado a la entrevista: %s" % self.entrevista

