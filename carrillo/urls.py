from django.conf.urls import patterns, include, url
from django.contrib import admin
import autocomplete_light.shortcuts as al
# import every app/autocomplete_light_registry.py
al.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'carrillo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^autocomplete/', include('autocomplete_light.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', "encuestas.views.relevamientos", name="home"),

    url(r'^gruposfamiliares/$',"encuestas.views.grupos_familiares", name="grupos_familiares"),
    url(r'^grupofamiliar/nuevo/$',"encuestas.views.grupo_familiar", name="grupo_familiar_create"),
    url(r'^grupofamiliar/(?P<id_grupofamiliar>\d+)/$',"encuestas.views.grupo_familiar", name="grupo_familiar_update"),

    url(r'^persona/(?P<id_persona>\d+)/$',"encuestas.views.vistapersona", name="persona"),

    url(r'^persona/$', "encuestas.views.vistapersona", name="persona"),
    url(r'^persona/(?P<id_persona>\d+)/$', "encuestas.views.vistapersona", name="persona"),
    url(r'^ajax/grupofamiliar/(?P<id_grupofamiliar>\d+)/persona/nueva/$', "encuestas.views.persona_create_modal", name="persona_create_modal"),
    url(r'^ajax/grupofamiliar/(?P<id_grupofamiliar>\d+)/persona/(?P<id_persona>\d+)/$', "encuestas.views.persona_update_modal", name="persona_update_modal"),
    url(r'^ajax/grupofamiliar/(?P<id_grupofamiliar>\d+)/persona/(?P<id_persona>\d+)/delete$', "encuestas.views.persona_delete_modal", name="persona_delete_modal"),

    # url(r'^ajax/persona/(?P<id_persona>\d+)/$',"encuestas.views.vistapersona", name = "persona"),

    url(r'^$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="auth_logout"),


    url(r'^entrevista/(?P<id_relevamiento>\d+)/nueva/$', 'encuestas.views.entrevista', name="entrevista_create"),
    url(r'^entrevista/(?P<id_relevamiento>\d+)/(?P<id_entrevista>\d+)/$', 'encuestas.views.entrevista', name="entrevista_update"),
    url(r'^entrevista/(?P<id_relevamiento>\d+)/(?P<id_entrevista>\d+)/carga/$', 'encuestas.views.entrevista_carga', name="entrevista_carga"),
    url(r'^entrevistas/(?P<id_relevamiento>\d+)/$', 'encuestas.views.entrevistas', name="entrevistas"),

    url(r'^capitalhumano/(?P<id_entrevista>\d+)/(?P<id_persona>\d+)/nuevo/$',"encuestas.views.capital_humano_create_modal", name="capital_humano_create_modal"),
    url(r'^capitalhumano/(?P<id_entrevista>\d+)/(?P<id_persona>\d+)/$',"encuestas.views.capital_humano_update_modal", name="capital_humano_update_modal"),

    url(r'^capitalsocial/$',"encuestas.views.Social", name = "capitalsocial"),
    url(r'^capitalsocial/(?P<id_capitalsocial>\d+)/$',"encuestas.views.Social", name = "capitalsocial"),
    url(r'^capitalfisico/$','encuestas.views.capital_fisico', name = "capitalfisico"),


    url(r'^reporte/(?P<id_relevamiento>\d+)/capitalsocial/$', "reportes.views.Reporte_CapitalSocial", name="reporte_capitalsocial"),
    url(r'^reporte/(?P<id_relevamiento>\d+)/capitalfisico/$',"reportes.views.Reporte_CapitalFisico", name="reporte_capitalfisico"),
    url(r'^reporte/(?P<id_relevamiento>\d+)/pap/$', "reportes.views.mujeres_con_pap", name="reporte_mujeres_con_pap"),
    url(r'^reporte/(?P<id_relevamiento>\d+)/descriptivo/$', "reportes.views.descriptivo", name="reporte_descriptivo"),
    url(r'^reporte/(?P<id_relevamiento>\d+)/tipo-familias/$', "reportes.views.tipo_familias", name="reporte_tipo_familias"),
    url(r'^reporte/(?P<id_relevamiento>\d+)/vulnerabilidades-capital-humano/$',"reportes.views.vulnerabilidad_cap_humano", name="reporte_vulnerabilidad_cap_humano"),


    url(r'^login/',"encuestas.views.Login", name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="auth_logout"),
    url(r'^contacto/$', "encuestas.views.contacto", name="conctacto"),
    # url(r'^relevamiento/$', "encuestas.views.relevamientos", name="relevamientos"),
    url(r'^grupofamiliar/(?P<id_grupofamiliar>\d+)/$',"encuestas.views.grupo_familiar", name = "grupofamiliar"),
)
