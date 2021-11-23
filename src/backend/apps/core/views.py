from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from apps.core.models import Room


def index(request):
    template_name = "index.html"
    context={}
    return render(request, template_name, context)

@login_required
def dashboard(request):
    template_name = "dashboard.html"
    context={}
    rooms= Room.objects.all()
    context['rooms'] = rooms
    if rooms.count() == 0:
        if request.user.is_superuser: 
            context['msg'] = "Comienza registrando algunos laboratorios desde tu panel de administración"
        elif request.user.is_staff:
            context['msg'] = "Contacta al admistrador del sistema para registrar laboratorios"
            
    return render(request, template_name, context)

@login_required
def administration(request):
    if request.user.is_superuser:        
        template_name = "dashboard.html"
        context={}
        
    return render(request, template_name, context)



