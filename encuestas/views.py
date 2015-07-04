from django.shortcuts import render, render_to_response
from django.views.forms import CapitalFisico_f, SocialModelForm
from encuestas.forms import Persona
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.decorators.debug import sensitive_post_parameters
from django.template.response import TemplateResponse
from django.shortcuts import resolve_url

def vistapersona(request):

    form=Persona()

    if request.POST:
        form=Persona(request.POST)

        if form.is_valid():
            
            grupo_familiar = form.cleaned_data['grupo_familiar']
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            sexo = form.cleaned_data['sexo']
            Fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            nacionalidad = form.cleaned_data['nacionalidad']
            dni = form.cleaned_data['dni']
            vinculo = form.cleaned_data['vinculo']
##          form.save() para guardar en la base de datos

            return render (request,'formulario.html', {'form': form})

    return render(request,'formulario.html', {'form': form})
            
def encuesta(request):

    return render_to_response('entrevista.html', locals(),context_instance=RequestContext(request))

def Social(request):
    form = SocialModelForm()
    if request.method == 'POST':
        form = SocialModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'exito.html',{'form':form})

            
    return render(request,'formulario.html',{'form':form})
    
def inicio(request):
    return render(request, 'site_base.html', {})

def CapitalFisico_p(request):
	form=CapitalFisico_f
	if request.method=="POST":
		form=CapitalFisico_f(request.POST)
		if form.is_valid():
			form.cleaned_data[i] for i in ('entrevista','habitaciones', 'propietario_terreno', 'situacion_vivienda','pisos','paredes','techo','calefaccion']
			
			return render(request,'formulario.html')
	return render(request,'formulario.html',{'form': form})
	