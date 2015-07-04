<<<<<<< HEAD
from django.shortcuts import render, render_to_response
from .forms import PersonaModelForm, CapitalSocialModelForm, CapitalFisicoModelForm
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.decorators.debug import sensitive_post_parameters
from django.template.response import TemplateResponse
from django.shortcuts import resolve_url


def vistapersona(request):

    form=PersonaModelForm()
    nombre = 'Formulario de persona'
    if request.POST:
        form=PersonaModelForm(request.POST)

        if form.is_valid():
            form.save() 

            return render (request,'exito.html', {'form': form})

    return render(request,'formulario.html', {'form': form,'nombre': nombre})
            
def encuesta(request):

    return render_to_response('entrevista.html', locals(),context_instance=RequestContext(request))

def Social(request):
    form = CapitalSocialModelForm()
    nombre = 'Formulario para capital social'
    if request.method == 'POST':
        form = CapitalSocialModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'exito.html',{'form':form})

            
    return render(request,'formulario.html',{'form':form, 'nombre': nombre})
    
def inicio(request):
    return render(request, 'site_base.html', {})

def inicio(request):
    return render(request, 'site_base.html', {})


def capital_fisico(request):
	form=CapitalFisicoModelForm()

	if request.method=="POST":
		form=CapitalFisicoModelForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request,'exito.html', {})
	return render(request,'formulario.html',{'form': form})