from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.decorators.debug import sensitive_post_parameters
from django.template.response import TemplateResponse
from django.shortcuts import resolve_url
from django.views.forms import CapitalFisico


@login_required
def encuesta(request):

    return render_to_response('entrevista.html', locals(),context_instance=RequestContext(request))

def CapitalFisico_p(request):
	form=CapitalFisico_f
	if request.method=="POST":
		form=CapitalFisico_f(request.POST)
		if form.is_valid():
			form.cleaned_data[i] for i in ('entrevista','habitaciones', 'propietario_terreno', 'situacion_vivienda','pisos','paredes','techo','calefaccion']
			
			return render(request,'formulario.html')
	return render(request,'formulario.html',{'form': form})
	
