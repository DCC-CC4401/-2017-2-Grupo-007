from django.shortcuts import render
from Denuncia.models import Denuncia
from django.http import HttpResponse
# Create your views here.
def muni(request):
    return render(request, 'muni.html', {})

def ultimasdenuncias(request):
    ult = Denuncia.objects.order_by('-fecha')[:5]
    return HttpResponse(output)

def tablas(request):
    return render(request, 'TablasMuni.html', {})