from django.shortcuts import render
<<<<<<< HEAD
from .forms import CapitalSocial
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.views.decorators.debug import sensitive_post_parameters
from django.template.response import TemplateResponse
from django.shortcuts import resolve_url


@login_required
def encuesta(request):

    return render_to_response('entrevista.html', locals(),context_instance=RequestContext(request))

def Social(request):
    form = CapitalSocial()
    if request.method == 'POST':
        form = CapitalSocial(request.POST)
    return render(request,'clase_social.html',{'form':form})
    


=======


def inicio(request):
    return render(request, 'site_base.html', {})
>>>>>>> fd662f9f61b3999bab7e0a2f3afe6b204cdf58c9
