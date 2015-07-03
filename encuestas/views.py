from django.shortcuts import render


def inicio(request):
    return render(request, 'site_base.html', {})
