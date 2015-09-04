from django.shortcuts import render, render_to_response, get_object_or_404
from .forms import PersonaModelForm, CapitalSocialModelForm, CapitalFisicoModelForm,GrupoFamiliarModelForm
from .models import CapitalSocial, GrupoFamiliar, CapitalSocial, CapitalSocial
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.decorators.debug import sensitive_post_parameters
from django.template.response import TemplateResponse
from django.shortcuts import resolve_url

def inicio(request):

    return render_to_response('inicio.html', locals(),context_instance=RequestContext(request))

def vistapersona(request):

    form=PersonaModelForm()
    nombre = 'Formulario de persona'
    if request.POST:
        form=PersonaModelForm(request.POST)

        if form.is_valid():
            form.save() 

            return render (request,'exito.html', {'form': form})

    return render(request,'formulario.html', {'form': form, 'nombre': nombre})

def encuesta(request):

    return render_to_response('CapitalSocial.html', locals(),context_instance=RequestContext(request))



def Social(request, id_capitalsocial=None):
    if id_capitalsocial:
        instance = get_object_or_404(CapitalSocial, id=id_capitalsocial)
    else:
        instance = None
    form = CapitalSocialModelForm(instance=instance)
    nombre = 'Formulario para capital social'
    if request.method == 'POST':
        form = CapitalSocialModelForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return render(request,'exito.html',{'form':form})

            
    return render(request,'formulario.html',{'form':form, 'nombre': nombre})
    


def capital_fisico(request):
    form=CapitalFisicoModelForm()

    if request.method=="POST":
        form=CapitalFisicoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'exito.html', {})
    return render(request,'formulario.html',{'form': form})

def Grupo_Familiar(request, id_grupofamiliar = None):
    if id_grupofamiliar:
        instance = get_object_or_404(GrupoFamiliar, id=id_grupofamiliar)
    else:
        instance = None
    form = GrupoFamiliarModelForm(instance = instance)
    nombre = 'Formulario para Grupo Familiar'
    if request.method=="POST":
        form=GrupoFamiliarModelForm(request.POST, instance = instance)
        if form.is_valid():
            form.save()
            return render(request,'exito.html', {'form': form})

    return render(request,'formulario.html',{'form': form, 'nombre': nombre})

def Reporte_CapitalSocial(request, id_capitalsocial=None):
	total=CapitalSocial.objects.filter(entrevista__relevamiento__id=1).count()
	con_energia=CapitalSocial.objects.filter(entrevista__relevamiento__id=1,energia_electrica=True).count()
	energia_porcentage=(con_energia/total)*100
	con_recoleccion_residuos=CapitalSocial.objects.filter(entrevista__relevamiento_id=1,recoleccion_residuo=True).count()
	recoleccion_porcentage=(con_recoleccion_residuos/total)*100
	con_transporte_publico=CapitalSocial.objects.filter(entrevista__relevamiento__id=1,transporte_publico=True).count()
	transporte_porcentage=(con_transporte_publico/total)*100
	con_pavimentacion=CapitalSocial.objects.filter(entrevista__relevamiento__id=1,calle_pavimentada=True).count()
	pavimentacion_porcentage=(con_pavimentacion/total)*100
	con_jardin_infantes=CapitalSocial.objects.filter(entrevista__relevamiento__id=1,jardin_infantes=True).count()
	jardin_porcentage=(con_jardin_infantes/total)*100
	con_escuela_primaria=CapitalSocial.objects.filter(entrevista__relevamiento__id=1,escuela_primaria=True).count()
	primaria_porcentage=(con_escuela_primaria/total)*100
	con_escuela_secundaria=CapitalSocial.objects.filter(entrevista__relevamiento__id=1,escuela_secundaria=True).count()
	secundaria_porcentage=(con_escuela_secundaria/total)*100
	con_comisaria=CapitalSocial.objects.filter(entrevista__relevamiento__id=1,comisaria=True).count()
	comisaria_porcentage=(con_comisaria/total)*100
	con_bomberos=CapitalSocial.objects.filter(entrevista__relevamiento__id=1,bomberos=True).count()
	bomberos_porcentage=(con_bomberos/total)*100
	return render(request, 'capitalsocial.html', {'energia_porcentage': energia_porcentage, 'pavimentacion_porcentage': pavimentacion_porcentage,'recoleccion_porcentage':recoleccion_porcentage,'transporte_porcentage':transporte_porcentage,'jardin_porcentage': jardin_porcentage,'primaria_porcentage':primaria_porcentage,'secundaria_porcentage':secundaria_porcentage,'comisaria_porcentage':comisaria_porcentage,'bomberos_porcentage':bomberos_porcentage})
	
	