# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, render_to_response, get_object_or_404
from .forms import (PersonaModelForm, CapitalSocialModelForm, CapitalFisicoModelForm, GrupoFamiliarModelForm,
                    LoginForm, CapitalHumanoModelForm, EntrevistaModelForm, OtrosDatosModelForm, RespuestaEntrevistaModelForm, BuscadorForm)
from .models import CapitalSocial, GrupoFamiliar, Entrevista, Relevamiento, Persona, CapitalFisico, Pregunta, RespuestaEntrevista
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.views.decorators.debug import sensitive_post_parameters
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from django_modalview.generic.edit import ModalCreateView, ModalUpdateView, ModalDeleteView
from django_modalview.generic.component import ModalResponse, ModalButton
from django.views.generic.edit import FormView
from django.views import generic
from django.contrib import messages
from encuestas.forms import ContactForm
from django.db.models import Q


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

    if 'grupo_familiar' in request.GET:
        gf_inicial = GrupoFamiliar.objects.get(id=request.GET['grupo_familiar'])
    else:
        gf_inicial = None

    form = EntrevistaModelForm(instance=instance, data=request.POST if request.method == 'POST' else None, initial={'grupo_familiar': gf_inicial})
    if form.is_valid():

        entrevista = form.save(commit=False)
        entrevista.relevamiento = relevamiento
        entrevista.cargado_por = request.user
        entrevista.save()
        entrevista.entrevistadores.add(request.user)
        return redirect(reverse('entrevista_carga', args=[relevamiento.id, entrevista.id]))

    return render(request,'entrevista.html', {'form': form,
        'nombre': 'Entrevista', 'button_text': 'Continuar'})


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

    forms_respuestas = []
    for preg in Pregunta.objects.filter(activa=True).order_by('id'):
        try:
            respuesta = RespuestaEntrevista.objects.get(pregunta=preg, entrevista=entrevista)
        except RespuestaEntrevista.DoesNotExist:
            respuesta = None
        fr = RespuestaEntrevistaModelForm(instance=respuesta, prefix='preg_%i' % preg.id, initial={'pregunta': preg, 'entrevista': entrevista},
                                          data=request.POST.copy() if request.method == 'POST' else None)
        forms_respuestas.append((preg, fr))
        if request.method == 'POST' and fr.is_valid():
            r = fr.save(commit=False)
            if r.id or r.respuesta:
                # solo guardar la instancia si ya existia o efectivamente fue respondida
                r.save()

        elif request.method == 'POST':
            todos_validos = False
    if not todos_validos:
        messages.error(request, 'Hay errores en el cuestionario')



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

    capitales_humanos_existentes = Persona.objects.filter(capitales_humanos__entrevista=entrevista)

    context = locals().copy()

    return render(request,'entrevista_carga.html', context)


class RelevamientosListView(generic.list.ListView):
    template_name = "relevamientos.html"
    model = Relevamiento

relevamientos = login_required(RelevamientosListView.as_view())


class EntrevistasListView(generic.list.ListView):
    template_name = "entrevistas.html"
    model = Entrevista

    def get_queryset(self):
        self.relevamiento = get_object_or_404(Relevamiento, id=self.kwargs['id_relevamiento'])
        qs = Entrevista.objects.filter(relevamiento=self.relevamiento)
        if "buscador" in self.request.GET:
            apellido = self.request.GET['buscador']
            condicion1 = Q(grupo_familiar__miembros__apellido__icontains= apellido)
            condicion2 = Q(grupo_familiar__apellido_principal__icontains= apellido)
            return qs.filter(condicion1 | condicion2).distinct()
        else:
            return qs



    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(EntrevistasListView, self).get_context_data(**kwargs)
        # Add in the publisher
        context['relevamiento'] = self.relevamiento
        context['buscador'] = BuscadorForm()
        return context


entrevistas = login_required(EntrevistasListView.as_view())


class GrupoFamiliarListView(generic.list.ListView):
    template_name = "grupos_familiares.html"
    model = GrupoFamiliar

    def get_queryset(self):
        if "buscador" in self.request.GET:
            apellido = self.request.GET['buscador']
            return GrupoFamiliar.objects.filter(apellido_principal__icontains= apellido).distinct()
        else:
            return GrupoFamiliar.objects.all()


    def get_context_data(self, **kwargs):
        context = super(GrupoFamiliarListView, self).get_context_data( **kwargs)
        context['buscador'] = BuscadorForm()
        return context



grupos_familiares = login_required(GrupoFamiliarListView.as_view())


class PersonaCreateModal(ModalCreateView):

    def __init__(self, *args, **kwargs):
        super(PersonaCreateModal, self).__init__(*args, **kwargs)
        self.title = "Agregar persona al grupo familiar"
        self.submit_button = ModalButton('Guardar', button_type='primary')
        self.close_button = ModalButton('Cerrar')
        self.delete_button=ModalButton('Eliminar')

        self.form_class = PersonaModelForm

    def dispatch(self, request, *args, **kwargs):
        # I get an user in the db with the id parameter that is in the url.
        self.grupo = GrupoFamiliar.objects.get(id=self.kwargs['id_grupofamiliar'])
        return super(PersonaCreateModal, self).dispatch(request, *args, **kwargs)

    def get_initial(self):
        return {'grupo_familiar': self.grupo, 'apellido': self.grupo.apellido_principal}

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
        self.submit_button = ModalButton('Guardar', button_type='primary')
        self.close_button = ModalButton('Cerrar')

    def dispatch(self, request, *args, **kwargs):
        # I get an user in the db with the id parameter that is in the url.
        self.object = Persona.objects.get(pk=kwargs.get('id_persona'), grupo_familiar__id=kwargs.get('id_grupofamiliar'))
        return super(PersonaUpdateModal, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form, **kwargs):
        i = form.save()
        self.response = ModalResponse("{obj} se actualizó correctamente".format(obj=i), 'success')
        return super(PersonaUpdateModal, self).form_valid(form, commit=False, **kwargs)


class PersonaDeleteModal(ModalDeleteView):
    def __init__(self, *args, **kwargs):
        super(PersonaDeleteModal, self).__init__(*args, **kwargs)
        self.title = "Eliminar persona"
        self.submit_button = ModalButton('Eliminar', button_type='danger')
        self.close_button = ModalButton('Cancelar',  button_type='default')
       
    def dispatch (self, request, *args, **kwargs):

        self.object = Persona.objects.get(id=kwargs.get('id_persona'), grupo_familiar__id=kwargs.get('id_grupofamiliar'))
        
        self.description = "¿Seguro que desea eliminar a %s?" % self.object
        return super(PersonaDeleteModal, self).dispatch(request, *args, **kwargs)
        

    def delete(self, request, *args, **kwargs):
        
        capitales_asociados = self.object.capitales_humanos.count()

        if capitales_asociados:
            self.response = ModalResponse("la persona no se puede eliminar porque tiene datos de entrevistas asociados", "warning")
        else:
            self.object.delete()
            self.response = ModalResponse("La persona fue eliminada", "success")


persona_create_modal = login_required(PersonaCreateModal.as_view())
persona_update_modal = login_required(PersonaUpdateModal.as_view())
persona_delete_modal = login_required(PersonaDeleteModal.as_view())


class CapitalHumanoCreateModal(ModalCreateView):

    def __init__(self, *args, **kwargs):
        super(CapitalHumanoCreateModal, self).__init__(*args, **kwargs)
        self.title = "Agregar capital humano"
        self.form_class = CapitalHumanoModelForm
        self.submit_button = ModalButton('Guardar', button_type='primary')
        self.close_button = ModalButton('Cerrar')

    def dispatch(self, request, *args, **kwargs):
        # I get an user in the db with the id parameter that is in the url.
        self.persona = Persona.objects.get(id=self.kwargs['id_persona'])
        self.entrevista = Entrevista.objects.get(id=self.kwargs['id_entrevista'])
        return super(CapitalHumanoCreateModal, self).dispatch(request, *args, **kwargs)

    def get_initial(self):
        return {'entrevista': self.entrevista, 'persona': self.persona}

    def form_valid(self, form, **kwargs):
        i = form.save()
        self.response = ModalResponse("{obj} se agregó correctamente".format(obj=i), 'success')
        return super(CapitalHumanoCreateModal, self).form_valid(form, **kwargs)


class CapitalHumanoUpdateModal(ModalUpdateView):

    def __init__(self, *args, **kwargs):
        super(CapitalHumanoUpdateModal, self).__init__(*args, **kwargs)
        self.title = "Editar capital humano"
        self.form_class = CapitalHumanoModelForm
        self.submit_button = ModalButton('Guardar', button_type='primary')
        self.close_button = ModalButton('Cerrar')

    def dispatch(self, request, *args, **kwargs):
        # I get an user in the db with the id parameter that is in the url.
        self.object = CapitalHumano.objects.get(persona__id=kwargs.get('id_persona'), entrevista__id=kwargs.get('id_entrevista'))
        return super(CapitalHumanoUpdateModal, self).dispatch(request, *args, **kwargs)

    def get_initial(self):
        return {'entrevista': self.object.entrevista, 'persona': self.object.persona}

    def form_valid(self, form, **kwargs):
        i = form.save()
        self.response = ModalResponse("{obj} se actualizó correctamente".format(obj=i), 'success')
        return super(CapitalHumanoUpdateModal, self).form_valid(form, commit=False, **kwargs)

capital_humano_create_modal = login_required(CapitalHumanoCreateModal.as_view())
capital_humano_update_modal = login_required(CapitalHumanoUpdateModal.as_view())




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
        form=GrupoFamiliarModelForm(request.POST, instance=instance)
        if form.is_valid():
            gf = form.save()
            if 'guardar' in request.POST:
                return redirect(reverse('grupo_familiar_update', args=[gf.id]))

            else:
                relevamiento = [clave for clave in request.POST.keys() if clave.startswith('entrevista')][0]
                relevamiento_id = int(relevamiento.split('_')[1])
                return redirect(reverse('entrevista_create', args=[relevamiento_id]) + '?grupo_familiar=%i' % gf.id)


    relevamientos = Relevamiento.objects.filter(activo=True)
    return render(request,'grupo_familiar.html',{'form': form, 'nombre': nombre, 'form_persona': form_persona, 'relevamientos':relevamientos})



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

