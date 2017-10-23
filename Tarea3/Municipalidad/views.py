from django.shortcuts import render
from Denuncia.models import Denuncia
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def muni(request):
    return render(request, 'muni.html', {})


def ultimasdenuncias(request):
    ult_list = Denuncia.objects.filter(comuna='SA')  # foreign key a comuna del usuario
    ult_list.order_by('-fecha')[:5]
    template = loader.get_template('estadisticas1.html')
    context = {
        'ult_list': ult_list,
    }
    return HttpResponse(template.render(context, request))


def tablas(request):
    return render(request, 'TablasMuni.html', {})
