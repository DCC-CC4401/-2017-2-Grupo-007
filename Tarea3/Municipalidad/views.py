from django.shortcuts import render
from Denuncia.models import Denuncia
from django.core.urlresolvers import reverse
from Municipalidad.models import Municipalidad
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template import loader
from .forms import Gestionar


# Create your views here.
def muni(request):
    muni = Municipalidad.objects.get(administrador_id=request.user.id)

    return render(request, 'muni.html', {'muni': muni})


def ultimasdenuncias(request):
    if request.user.is_authenticated:
        muni = Municipalidad.objects.get(administrador_id=request.user.id)
        comuna_actual = muni.comuna
        ult_list = Denuncia.objects.filter(comuna=comuna_actual)
        ult_list.order_by('-fecha')[:5]
        template = loader.get_template('estadisticas1.html')
        context = {
            'muni': muni,
            'ult_list': ult_list,
        }
        print(context)
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/')


def tablas(request):
    return render(request, 'TablasMuni.html', {})


def detalles(request, denuncia_id):
    data = Denuncia.objects.filter(id=denuncia_id)
    form = Gestionar()
    template = loader.get_template('detalles.html')
    context = {
        'data': data,
        'form': form
    }

    return HttpResponse(template.render(context, request))


def chartsPageMuni(request):
    muni = Municipalidad.objects.get(usuario_id=request.user.id)
    comuna = muni.comuna
    # comuna='SA'
    numDenReportadas = Denuncia.objects.filter(comuna=comuna, estado='RE').count()
    numDenConsolidadas = Denuncia.objects.filter(comuna=comuna, estado='CO').count()
    numDenVerificadas = Denuncia.objects.filter(comuna=comuna, estado='VE').count()
    numDenCerradas = Denuncia.objects.filter(comuna=comuna, estado='CE').count()
    numDenDesechadas = Denuncia.objects.filter(comuna=comuna, estado='DE').count()
    totalDen = numDenReportadas + numDenConsolidadas + numDenVerificadas + numDenCerradas + numDenDesechadas
    numEstComuna = 18  # consulta dummy
    numEstTotal = 149
    if request.user.is_authenticated:
        # muni = Municipalidad.objects.get(usuario_id=request.user.id)
        # comuna = muni.comuna
        comuna = 'SA'
        numDenReportadas = Denuncia.objects.filter(comuna=comuna, estado='RE').count()
        numDenConsolidadas = Denuncia.objects.filter(comuna=comuna, estado='CO').count()
        numDenVerificadas = Denuncia.objects.filter(comuna=comuna, estado='VE').count()
        numDenCerradas = Denuncia.objects.filter(comuna=comuna, estado='CE').count()
        numDenDesechadas = Denuncia.objects.filter(comuna=comuna, estado='DE').count()
        totalDen = numDenReportadas + numDenConsolidadas + numDenVerificadas + numDenCerradas + numDenDesechadas
        numEstComuna = 18  # consulta dummy
        numEstTotal = 149  # consulta dummy

        template = loader.get_template('chartsPageMuni.html')
        context = {
            'numEstComuna': numEstComuna,
            'numEstTotal': numEstTotal,
            'comuna': comuna,
            'numDenReportadas': numDenReportadas,
            'numDenConsolidadas': numDenConsolidadas,
            'numDenVerificadas': numDenVerificadas,
            'numDenCerradas': numDenCerradas,
            'numDenDesechadas': numDenDesechadas,
            'totalDen': totalDen
        }
        print(context)
        return HttpResponse(template.render(context, request))

    else:
        return HttpResponseRedirect('/')



def gestion(request, denuncia_id):
    if request.POST:
        estado = request.POST.get('estado')
        data = Denuncia.objects.get(id=denuncia_id)
        data.estado = estado
        data.save()
        return HttpResponseRedirect(reverse('municipalidad:ultimasdenuncias'))

    else:
        form = Gestionar()
        return render(request, 'detalles.html', {'form': form})
