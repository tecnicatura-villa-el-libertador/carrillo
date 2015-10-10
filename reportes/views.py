from django.db.models import Avg, Count
from django.utils.timezone import now
from django.db.models import Q
from datetime import timedelta
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from encuestas.models import Relevamiento, CapitalSocial, CapitalFisico, Persona, GrupoFamiliar, Entrevista
from reportes.forms import ReporteForm
from django.http import Http404

@login_required
def mujeres_con_pap(request, id_relevamiento):
    try:
        relevamiento = get_object_or_404(Relevamiento, id=id_relevamiento)
        nombre = 'Porcentaje de mujeres con PAP'
        mujeres_con_pap = Persona.objects.filter(grupo_familiar__entrevistas__relevamiento=relevamiento, sexo='f', capitales_humanos__pap=True).count()
        mujeres_total = Persona.objects.filter(grupo_familiar__entrevistas__relevamiento=relevamiento, sexo='f').count()

        total = (mujeres_con_pap/mujeres_total)*100 if mujeres_total else '--'

        return render(request,'pap.html',{'nombre': nombre, 'total': total})
    except Relevamiento.DoesNotExist:
        raise Http404("El relevamiento no existe")


@login_required
def Reporte_CapitalSocial(request, id_relevamiento):
    relevamiento = get_object_or_404(Relevamiento, id=id_relevamiento)

    total=CapitalSocial.objects.filter(entrevista__relevamiento=relevamiento).count()
    con_energia=CapitalSocial.objects.filter(entrevista__relevamiento=relevamiento, energia_electrica=True).count()
    energia_porcentaje=(con_energia/total)*100
    con_recoleccion_residuos=CapitalSocial.objects.filter(entrevista__relevamiento_id=1,recoleccion_residuo=True).count()
    recoleccion_porcentaje=(con_recoleccion_residuos/total)*100
    con_transporte_publico=CapitalSocial.objects.filter(entrevista__relevamiento=relevamiento, transporte_publico=True).count()
    transporte_porcentaje=(con_transporte_publico/total)*100
    con_pavimentacion=CapitalSocial.objects.filter(entrevista__relevamiento=relevamiento, calle_pavimentada=True).count()
    pavimentacion_porcentaje=(con_pavimentacion/total)*100
    con_jardin_infantes=CapitalSocial.objects.filter(entrevista__relevamiento=relevamiento, jardin_infantes=True).count()
    jardin_porcentaje=(con_jardin_infantes/total)*100
    con_escuela_primaria=CapitalSocial.objects.filter(entrevista__relevamiento=relevamiento, escuela_primaria=True).count()
    primaria_porcentaje=(con_escuela_primaria/total)*100
    con_escuela_secundaria=CapitalSocial.objects.filter(entrevista__relevamiento=relevamiento, escuela_secundaria=True).count()
    secundaria_porcentaje=(con_escuela_secundaria/total)*100
    con_comisaria=CapitalSocial.objects.filter(entrevista__relevamiento=relevamiento, comisaria=True).count()
    comisaria_porcentaje=(con_comisaria/total)*100
    con_bomberos=CapitalSocial.objects.filter(entrevista__relevamiento=relevamiento, bomberos=True).count()
    bomberos_porcentaje=(con_bomberos/total)*100
    return render(request, 'capitalsocial.html', {'energia_porcentaje': energia_porcentaje, 'pavimentacion_porcentaje': pavimentacion_porcentaje,'recoleccion_porcentaje':recoleccion_porcentaje,'transporte_porcentaje':transporte_porcentaje,'jardin_porcentaje': jardin_porcentaje,'primaria_porcentaje':primaria_porcentaje,'secundaria_porcentaje':secundaria_porcentaje,'comisaria_porcentaje':comisaria_porcentaje,'bomberos_porcentaje':bomberos_porcentaje})


def Reporte_CapitalFisico(request, id_relevamiento):
    relevamiento = get_object_or_404(Relevamiento, id=id_relevamiento)
    total = CapitalFisico.objects.filter (entrevista__relevamiento=relevamiento).count()
    es_propietarioTerreno=CapitalFisico.objects.filter(entrevista__relevamiento=relevamiento, propietario_terreno=True).count()
    propietarioTerreno_porcentaje= (es_propietarioTerreno/total)*100
    tiene_pisos=CapitalFisico.objects.filter(entrevista__relevamiento=relevamiento, pisos=True).count()
    pisos_porcentaje=(tiene_pisos/total)*100
    tiene_techo=CapitalFisico.objects.filter(entrevista__relevamiento=relevamiento, techo=True).count()
    techo_porcentaje=(tiene_techo/total)*100
    tiene_paredes=CapitalFisico.objects.filter(entrevista__relevamiento_id=1, paredes=True).count()
    paredes_porcentaje=(tiene_paredes/total)*100
    propietario_vivienda=CapitalFisico.objects.filter(entrevista__relevamiento=relevamiento, situacion_vivienda='propietarioVivienda').count()
    propietario_vivienda_porcentaje=(propietario_vivienda/total)*100
    en_comodato=CapitalFisico.objects.filter(entrevista__relevamiento=relevamiento, situacion_vivienda='comodato').count()
    comodato_porcentaje=(en_comodato/total)*100
    en_alquiler=CapitalFisico.objects.filter(entrevista__relevamiento=relevamiento, situacion_vivienda='alquiler').count()
    alquiler_porcentaje=(en_alquiler/total)*100
    es_otro=CapitalFisico.objects.filter(entrevista__relevamiento=relevamiento, situacion_vivienda='otro').count()
    porcentaje_es_otro=(es_otro/total)*100
    tiene_calefaccion_natural=CapitalFisico.objects.filter(entrevista__relevamiento=relevamiento, calefaccion='gas_natural').count()
    calefaccion_natural_porcentaje=(tiene_calefaccion_natural/total)*100
    tiene_calefaccion_envasado=CapitalFisico.objects.filter(entrevista__relevamiento=relevamiento, calefaccion='gas_envasado').count()
    calefaccion_envasado_porcentaje=(tiene_calefaccion_envasado/total)*100
    cantidad_habitaciones = CapitalFisico.objects.filter(entrevista__relevamiento=relevamiento).aggregate(Avg('habitaciones'))
    return render(request, 'capitalfisico.html',{'propietarioTerreno_porcentaje':propietarioTerreno_porcentaje, 'pisos_porcentaje': pisos_porcentaje, 'techo_porcentaje':techo_porcentaje, 'paredes_porcentaje':paredes_porcentaje,'propietario_vivienda_porcentaje':propietario_vivienda_porcentaje,'comodato_porcentaje':comodato_porcentaje,'alquiler_porcentaje':alquiler_porcentaje,'porcentaje_es_otro':porcentaje_es_otro,'calefaccion_natural_porcentaje':calefaccion_natural_porcentaje,'calefaccion_envasado_porcentaje':calefaccion_envasado_porcentaje,'cantidad_habitaciones':cantidad_habitaciones['habitaciones__avg']})


@login_required
def descriptivo(request, id_relevamiento):

    def columna(relevamiento):
        hogares = GrupoFamiliar.objects.filter(entrevistas__relevamiento=relevamiento)

        # grupos familiares con la misma direccion
        total_lotes = hogares.values('direccion').distinct().count()
        total_hogares = hogares.count()

        total_personas = Persona.objects.filter(grupo_familiar__in=hogares).count()   # hogares.annotate(cantidad_miembros=Sum('miembros')).aggregate(Sum('cantidad_miembros'))
        promedio_personas = total_personas / total_hogares

        mujeres = Persona.objects.filter(grupo_familiar__in=hogares, sexo='f').count()
        mujeres = {'total': mujeres, 'porcentaje': (mujeres / total_personas) * 100, 'promedio': mujeres / total_hogares}
        hombres = Persona.objects.filter(grupo_familiar__in=hogares, sexo='m').count()
        hombres = {'total': hombres, 'porcentaje': (hombres / total_personas) * 100, 'promedio': hombres / total_hogares}

        migrantes = Persona.objects.filter(grupo_familiar__in=hogares).exclude(nacionalidad='argentina').count()
        migrantes = {'total': migrantes, 'porcentaje': (migrantes / total_personas) * 100, 'promedio': migrantes / total_hogares}

        indocumentados = Persona.objects.filter(grupo_familiar__in=hogares, dni__isnull=True).count()
        indocumentados = {'total': indocumentados, 'porcentaje': (indocumentados / total_personas) * 100, 'promedio': indocumentados / total_hogares}

        return locals()

    relevamientos = [get_object_or_404(Relevamiento, id=id_relevamiento)]
    form = ReporteForm(data=request.GET or None)
    form.fields['relevamientos'].queryset = Relevamiento.objects.exclude(id=id_relevamiento)
    if form.is_valid():
        relevamientos += form.cleaned_data.get('relevamientos', [])
    columnas = [columna(relevamiento) for relevamiento in relevamientos]

    return render(request, 'reporte_descriptivo.html', {'columnas': columnas, 'form': form,
                                                        'relevamientos': relevamientos, 'titulo': 'Datos descriptivos'})



@login_required
def tipo_familias(request, id_relevamiento):

    def columna(relevamientos):
        return [(label, GrupoFamiliar.objects.filter(entrevistas__relevamiento=relevamiento, tipo_familia=tipo).count())
                for tipo, label in GrupoFamiliar.OPCIONES_TIPO_FAMILIA]

    relevamientos = [get_object_or_404(Relevamiento, id=id_relevamiento)]
    form = ReporteForm(data=request.GET or None)
    form.fields['relevamientos'].queryset = Relevamiento.objects.exclude(id=id_relevamiento)
    if form.is_valid():
        relevamientos += form.cleaned_data.get('relevamientos', [])

    columnas = []
    for tipo, label in GrupoFamiliar.OPCIONES_TIPO_FAMILIA:
        data = []
        for relevamiento in relevamientos:
            total = GrupoFamiliar.objects.filter(entrevistas__relevamiento=relevamiento).count()
            cuenta = GrupoFamiliar.objects.filter(entrevistas__relevamiento=relevamiento, tipo_familia=tipo).count()

            data.append({'cantidad': cuenta, 'porcentaje': cuenta*100/total, 'total': total})
        columnas.append((label, data))

    return render(request, 'reporte_tipos_familia.html', {'columnas': columnas, 'form': form,
                                                          'relevamientos': relevamientos, 'titulo': 'Tipos de familia'})



@login_required
def vulnerabilidad_cap_humano(request, id_relevamiento):
    desde = now() - timedelta(days=365*5)

    def columna(relevamiento):
        familias = GrupoFamiliar.objects.filter(entrevistas__relevamiento=relevamiento)
        total_familias = familias.count()
        familias_con_3menores = familias.extra(select = {"menores_count" : """
            SELECT COUNT(*) from encuestas_persona WHERE
                encuestas_persona.grupo_familiar_id = encuestas_grupofamiliar.id AND
                encuestas_persona.fecha_nacimiento >= {}""".format(desde.date())})
        familias_con_3menores = len([f for f in familias_con_3menores if f.menores_count >= 3])
        familias_monoparanteles_con_jefa = len([f for f in familias.filter(tipo_familia='monoparental') if f.jefe_familia and f.jefe_familia.sexo == 'f'])

        return locals()

    relevamientos = [get_object_or_404(Relevamiento, id=id_relevamiento)]
    form = ReporteForm(data=request.GET or None)
    form.fields['relevamientos'].queryset = Relevamiento.objects.exclude(id=id_relevamiento)
    if form.is_valid():
        relevamientos += form.cleaned_data.get('relevamientos', [])

    columnas = [columna(relevamiento) for relevamiento in relevamientos]

    return render(request, 'reporte_vulnerabilidad_cap_humano.html', {'columnas': columnas, 'form': form,
                                                                      'relevamientos': relevamientos, 'titulo': 'Datos descriptivos'})


