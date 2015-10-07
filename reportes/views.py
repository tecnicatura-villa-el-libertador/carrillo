from django.db.models import Avg
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from encuestas.models import Relevamiento, CapitalSocial, CapitalFisico, Persona


@login_required
def mujeres_con_pap(request, id_relevamiento):
    relevamiento = get_object_or_404(Relevamiento, id=id_relevamiento)
    nombre = 'Porcentaje de mujeres con PAP'
    mujeres_con_pap = Persona.objects.filter(grupo_familiar__entrevista__relevamiento=relevamiento, sexo='f', capitales_humanos__pap=True).count()
    mujeres_total = Persona.objects.filter(grupo_familiar__entrevista__relevamiento=relevamiento, sexo='f').count()

    total = (mujeres_con_pap/mujeres_total)*100 if mujeres_total else '--'

    return render(request,'pap.html',{'nombre': nombre, 'total': total})


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


