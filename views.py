from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def primeraFuncion(request):
    return render(request, 'landing.html')

def formularioContacto(request):
    return render(request, 'registro.html')