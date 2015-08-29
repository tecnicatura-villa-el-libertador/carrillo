from django.shortcuts import render,redirect, render_to_response, get_object_or_404, resolve_url
from .forms import PersonaModelForm, CapitalSocialModelForm, CapitalFisicoModelForm,GrupoFamiliarModelForm,LoginForm,CapitalHumanoModelForm
from .models import CapitalSocial, GrupoFamiliar, Relevamiento
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.debug import sensitive_post_parameters
from django.template.response import TemplateResponse


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

    return render_to_response('entrevista.html', locals(),context_instance=RequestContext(request))



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

def Login(request):
    nombre = "Formulario de login"
    form = LoginForm()
    next_url = request.GET.get('next', '/')
    if request.method =="POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect(request.POST.get('next', '/'))
                
    return render(request,'formulario.html',{'form': form, 'nombre': nombre,
                                             'next': next_url})
	
		
			
			


def capital_humano(request,id_capitalhumano=None):
    if id_capitalhumano:
        instance=get_object_or_404(CapitalHumano,id=id_capitalhumano)
    else:
        instance=None
    form=CapitalHumanoModelForm(instance=instance)
    nombre="formulario para capital humano"
    if request.method=='POST':
        form=CapitalHumanoModelForm(request.POST, instance=instance)
        if form.is_valid:
            form.save()
            return render(request, 'exito.html',{'form':form})
    return render(request, 'formulario.html',{'form':form,'nombre':nombre})

def relevamientoActivo(request):
    zona=Relevamiento.objects.filter(estado=True)
    return render (request, 'Relevamiento,html',{'zona':zona})

    
    
            

