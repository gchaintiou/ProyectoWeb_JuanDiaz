from django.shortcuts import render,HttpResponse
from .models import Servicio

# Create your views here.
def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicios/servicios.htm', {"servicios": servicios})