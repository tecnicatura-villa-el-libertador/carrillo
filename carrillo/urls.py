from django.conf.urls import patterns, include, url
from django.contrib import admin



urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'carrillo.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', "encuestas.views.inicio", name="home"),
    url(r'^persona/$', "encuestas.views.vistapersona", name="persona"),
    url(r'^persona/(?P<id_persona>\d+)/$',"encuestas.views.vistapersona", name = "persona"),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login',name="my_login"),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="auth_logout"),
    url(r'^capitalsocial/$',"encuestas.views.Social", name = "capitalsocial"),
    url(r'^capitalsocial/(?P<id_capitalsocial>\d+)/$',"encuestas.views.Social", name = "capitalsocial"),
    url(r'^capitalfisico/$','encuestas.views.capital_fisico', name = "capitalfisico"),
    url(r'^grupofamiliar/$',"encuestas.views.Grupo_Familiar", name = "grupofamiliar"),
    url(r'^capitalhumano/$',"encuestas.views.capital_humano", name="capitalhumano"),
    url(r'^grupofamiliar/(?P<id_grupofamiliar>\d+)/$',"encuestas.views.Grupo_Familiar", name = "grupofamiliar"),
    url(r'^relevamiento/$', "encuestas.views.relevamientoActivo", name="relevamientoActivo"),
	url(r'^reportepap/$', "encuestas.views.mujeres_con_pap", name="mujeres_con_pap"),
	url(r'^reporte/capitalsocial/$', "encuestas.views.Reporte_CapitalSocial"),
    url(r'^login/',"encuestas.views.Login", name = "login"),
    url(r'^relevamiento/$', "encuestas.views.relevamientoActivo", name="relevamientoActivo"),
	url(r'^reporte/capitalfisico/$',"encuestas.views.Reporte_CapitalFisico", name="Reporte_CapitalFisico"), )
