from django.shortcuts import render
from encuestas.forms import PersonaModelForm, CapitalFisicoModelForm


def vistapersona(request):

    form=PersonaModelForm()

    if request.POST:
        form=PersonaForm(request.POST)

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


def capital_fisico(request):
	form=CapitalFisicoModelForm()

	if request.method=="POST":
		form=CapitalFisicoModelForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request,'exito.html', {})
	return render(request,'formulario.html',{'form': form})
	
