from django.shortcuts import render
from django.views.forms import CapitalFisico_f
from encuestas.forms import Persona


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
	
