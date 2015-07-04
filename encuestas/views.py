from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.decorators.debug import sensitive_post_parameters
from django.template.response import TemplateResponse
from django.shortcuts import resolve_url
from encuestas.forms import Persona
from django.http import HttpResponse

@login_required
def encuesta(request):

    return render_to_response('entrevista.html', locals(),context_instance=RequestContext(request))

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

            return render (request,'formulario.html')

    return render(request,'formulario.html')
            

            
