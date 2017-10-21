from django.shortcuts import render
from .forms import DenunciaForm
from Persona.models import Persona
from Denuncia.models import Denuncia
from django.http import HttpResponseRedirect
# Create your views here.

def denunciar(request):
    if request.POST:
        print(request.POST)
        estado= request.POST.get('estado')
        lugar= request.POST.get('lugar')
        tipo = request.POST.get('tipo')
        sexo = request.POST.get('sexo')
        color = request.POST.get('color')
        herido = request.POST.get('herido')
        denunciar_obj= Denuncia(estado=estado, lugar=lugar, tipo=tipo, sexo= sexo, color=color, herido = herido)
        denunciar_obj.save()
        return HttpResponseRedirect('/')
    else:
        form = DenunciaForm()
        return render(request, 'denuncia.html', {'form': form})
