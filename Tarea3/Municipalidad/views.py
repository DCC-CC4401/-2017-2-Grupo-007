from django.shortcuts import render
from Denuncia.models import Denuncia
from django.http import HttpResponse
# Create your views here.
def muni(request):
    return render(request, 'muni.html', {})

def ultimas_denuncias(request):
    ult = Denuncia.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in ult])
    return HttpResponse(output)