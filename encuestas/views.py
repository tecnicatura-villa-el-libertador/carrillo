from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from .forms import (PersonaModelForm, CapitalSocialModelForm, CapitalFisicoModelForm, GrupoFamiliarModelForm,
                    LoginForm, CapitalHumanoModelForm, EntrevistaModelForm, OtrosDatosModelForm)
from .models import CapitalSocial, GrupoFamiliar, Entrevista, Relevamiento, Persona, CapitalFisico
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.debug import sensitive_post_parameters
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from django_modalview.generic.edit import ModalCreateView, ModalUpdateView
from django_modalview.generic.component import ModalResponse
from django.views.generic.edit import FormView
from django.db.models import Avg
from django.views import generic
from django.contrib import messages
from encuestas.forms import ContactForm


class ContactView(FormView):
    template_name = 'formulario.html'
    form_class = ContactForm
    success_url = '/'


    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        print("enviar mensaje a :")
        print(form.cleaned_data.get('nombre'))
        print(form.cleaned_data.get('mensaje'))
        return super(ContactView, self).form_valid(form)

contacto = ContactView.as_view()


@login_required
def entrevista(request, id_relevamiento, id_entrevista=None):

    if id_entrevista:
        instance = get_object_or_404(Entrevista, id=id_entrevista, relevamiento__id=id_relevamiento)
    else:
        instance = None
    relevamiento = get_object_or_404(Relevamiento, id=id_relevamiento)
    form = EntrevistaModelForm(instance=instance, data=request.POST if request.method == 'POST' else None)
    if form.is_valid():

        entrevista = form.save(commit=False)
        entrevista.relevamiento = relevamiento
        entrevista.cargado_por = request.user
        entrevista.save()
        entrevista.entrevistadores.add(request.user)
        return redirect(reverse('entrevista_carga', args=[relevamiento.id, entrevista.id]))

    return render(request,'entrevista.html', {'form': form, 'nombre': 'Entrevista', 'button_text': 'Guardar'})


@login_required
def entrevista_carga(request, id_relevamiento, id_entrevista):
    entrevista = get_object_or_404(Entrevista, id=id_entrevista, relevamiento__id=id_relevamiento)

    capital_fisico = entrevista.capital_fisico if hasattr(entrevista, 'capital_fisico') else None
    capital_social = entrevista.capital_social if hasattr(entrevista, 'capital_social') else None

    form_cf = CapitalFisicoModelForm(instance=capital_fisico, data=request.POST.copy() if request.method == 'POST' else None)
    form_cs = CapitalSocialModelForm(instance=capital_social, data=request.POST.copy() if request.method == 'POST' else None)
    form = OtrosDatosModelForm(instance=entrevista, data=request.POST.copy() if request.method == 'POST' else None)

    form.fields['entrevistado'].queryset = entrevista.grupo_familiar.miembros.all()


    todos_validos = True
    if form_cf.is_valid():
        cf = form_cf.save(commit=False)
        cf.entrevista = entrevista
        cf.save()
    elif request.method == 'POST':
        todos_validos = False
        messages.error(request, 'Hay errores en Capital Físico')

    if form_cs.is_valid():
        cs = form_cs.save(commit=False)
        cs.entrevista = entrevista
        cs.save()
    elif request.method == 'POST':
        todos_validos = False
        messages.error(request, 'Hay errores en Capital Social')

    if form.is_valid():
        form.save()
    elif request.method == 'POST':
        todos_validos = False
        messages.error(request, 'Hay errores en Otros datos')

    if request.method == 'POST' and todos_validos:
        messages.success(request, 'Todos los datos se guardaron correctamente')
        # recargar la pagina
        return redirect(request.META.get('HTTP_REFERER'))

    context = locals().copy()

    return render(request,'entrevista_carga.html', context)


class RelevamientosListView(generic.list.ListView):
    template_name = "relevamientos.html"
    model = Relevamiento

relevamientos = login_required(RelevamientosListView.as_view())


class GrupoFamiliarListView(generic.list.ListView):
    template_name = "grupos_familiares.html"
    model = GrupoFamiliar

grupos_familiares = login_required(GrupoFamiliarListView.as_view())


class PersonaCreateModal(ModalCreateView):

    def __init__(self, *args, **kwargs):
        super(PersonaCreateModal, self).__init__(*args, **kwargs)
        self.title = "Agregar persona al grupo familiar"
        self.form_class = PersonaModelForm

    def dispatch(self, request, *args, **kwargs):
        # I get an user in the db with the id parameter that is in the url.
        self.grupo = GrupoFamiliar.objects.get(id=self.kwargs['id_grupofamiliar'])
        return super(PersonaCreateModal, self).dispatch(request, *args, **kwargs)

    def get_form(self, form_class):
        form = super(PersonaCreateModal, self).get_form(form_class)
        form.initial = {'grupo_familiar': self.grupo, 'apellido': self.grupo.apellido_principal}
        return form

    def form_valid(self, form, **kwargs):
        #import ipdb; ipdb.set_trace()
        # i = self.save(form, commit=False)               # When you save the form an attribute name object is created.
        i = form.save()
        self.response = ModalResponse("{obj} se agregó correctamente".format(obj=i), 'success')
        return super(PersonaCreateModal, self).form_valid(form, **kwargs)


class PersonaUpdateModal(ModalUpdateView):

    def __init__(self, *args, **kwargs):
        super(PersonaUpdateModal, self).__init__(*args, **kwargs)
        self.title = "Editar persona"
        self.form_class = PersonaModelForm

    def dispatch(self, request, *args, **kwargs):
        # I get an user in the db with the id parameter that is in the url.
        self.object = Persona.objects.get(pk=kwargs.get('id_persona'), grupo_familiar__id=kwargs.get('id_grupofamiliar'))
        return super(PersonaUpdateModal, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form, **kwargs):
        i = form.save()
        self.response = ModalResponse("{obj} se actualizó correctamente".format(obj=i), 'success')
        return super(PersonaUpdateModal, self).form_valid(form, commit=False, **kwargs)

persona_create_modal = login_required(PersonaCreateModal.as_view())
persona_update_modal = login_required(PersonaUpdateModal.as_view())



@login_required
def inicio(request):
    return render_to_response('inicio.html', locals(),context_instance=RequestContext(request))


@login_required
def vistapersona(request, id_persona=None):
    if id_persona:
        instance = get_object_or_404(Persona, id=id_persona)
    else:
        instance = None
    form = PersonaModelForm(instance = instance)
    nombre = 'Formulario de persona'
    if request.method == 'POST':
        form = PersonaModelForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return render (request,'exito.html', {'form': form})

    return render(request,'formulario.html', {'form': form, 'nombre': nombre})



@login_required
def Social(request, id_capitalsocial=None):
    if id_capitalsocial:
        instance = get_object_or_404(CapitalSocial, id=id_capitalsocial)
    else:
        instance = None
    form = CapitalSocialModelForm(instance = instance)
    nombre = 'Formulario para capital social'
    if request.method == 'POST':
        form = CapitalSocialModelForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return render(request,'exito.html',{'form':form})

    return render(request,'formulario.html',{'form':form, 'nombre': nombre})



@login_required
def capital_fisico(request):
    form = CapitalFisicoModelForm()

    if request.method=="POST":
        form = CapitalFisicoModelForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'exito.html', {})
    return render(request,'formulario.html',{'form': form})


@login_required
def grupo_familiar(request, id_grupofamiliar = None):
    if id_grupofamiliar:
        instance = get_object_or_404(GrupoFamiliar, id=id_grupofamiliar)
    else:
        instance = None
    form_persona = PersonaModelForm()
    form = GrupoFamiliarModelForm(instance = instance)
    nombre = 'Grupo Familiar'
    if request.method=="POST":
        form=GrupoFamiliarModelForm(request.POST, instance = instance)
        if form.is_valid():
            form.save()
            return render(request,'exito.html', {'form': form})

    return render(request,'grupo_familiar.html',{'form': form, 'nombre': nombre, 'form_persona': form_persona})



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


@login_required
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


def mujeres_con_pap(request):
    nombre = 'Porcentaje de mujeres con PAP'
    mujeres_con_pap = Persona.objects.filter(grupo_familiar__entrevista__relevamiento__id=1, sexo='f', capitales_humanos__pap=True)
    mujeres_con_pap=len(mujeres_con_pap)
    mujeres_total=Persona.objects.filter(grupo_familiar__entrevista__relevamiento__id=1, sexo='f')
    mujeres_total=len(mujeres_total)
    total=(mujeres_con_pap/mujeres_total)*100

    return render(request,'pap.html',{'nombre': nombre, 'total': total})


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


def Reporte_CapitalFisico(request, id_capitalfisico=None):
    total=CapitalFisico.objects.filter (entrevista__relevamiento__id=1).count()
    es_propietarioTerreno=CapitalFisico.objects.filter(entrevista__relevamiento__id=1, propietario_terreno=True).count()
    propietarioTerreno_porcentaje= (es_propietarioTerreno/total)*100
    tiene_pisos=CapitalFisico.objects.filter(entrevista__relevamiento__id=1, pisos=True).count()
    pisos_porcentaje=(tiene_pisos/total)*100
    tiene_techo=CapitalFisico.objects.filter(entrevista__relevamiento__id=1, techo=True).count()
    techo_porcentaje=(tiene_techo/total)*100
    tiene_paredes=CapitalFisico.objects.filter(entrevista__relevamiento_id=1, paredes=True).count()
    paredes_porcentaje=(tiene_paredes/total)*100
    propietario_vivienda=CapitalFisico.objects.filter(entrevista__relevamiento__id=1, situacion_vivienda='propietarioVivienda').count()
    propietario_vivienda_porcentaje=(propietario_vivienda/total)*100
    en_comodato=CapitalFisico.objects.filter(entrevista__relevamiento__id=1, situacion_vivienda='comodato').count()
    comodato_porcentaje=(en_comodato/total)*100
    en_alquiler=CapitalFisico.objects.filter(entrevista__relevamiento__id=1, situacion_vivienda='alquiler').count()
    alquiler_porcentaje=(en_alquiler/total)*100
    es_otro=CapitalFisico.objects.filter(entrevista__relevamiento__id=1, situacion_vivienda='otro').count()
    porcentaje_es_otro=(es_otro/total)*100
    tiene_calefaccion_natural=CapitalFisico.objects.filter(entrevista__relevamiento__id=1,calefaccion='gas_natural').count()
    calefaccion_natural_porcentaje=(tiene_calefaccion_natural/total)*100
    tiene_calefaccion_envasado=CapitalFisico.objects.filter(entrevista__relevamiento__id=1,calefaccion='gas_envasado').count()
    calefaccion_envasado_porcentaje=(tiene_calefaccion_envasado/total)*100

    cantidad_habitaciones=CapitalFisico.objects.filter(entrevista__relevamiento__id=1).aggregate(Avg('habitaciones'))


    return render(request, 'capitalfisico.html',{'propietarioTerreno_porcentaje':propietarioTerreno_porcentaje, 'pisos_porcentaje': pisos_porcentaje, 'techo_porcentaje':techo_porcentaje, 'paredes_porcentaje':paredes_porcentaje,'propietario_vivienda_porcentaje':propietario_vivienda_porcentaje,'comodato_porcentaje':comodato_porcentaje,'alquiler_porcentaje':alquiler_porcentaje,'porcentaje_es_otro':porcentaje_es_otro,'calefaccion_natural_porcentaje':calefaccion_natural_porcentaje,'calefaccion_envasado_porcentaje':calefaccion_envasado_porcentaje,'cantidad_habitaciones':cantidad_habitaciones['habitaciones__avg']})

