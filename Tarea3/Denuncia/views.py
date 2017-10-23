from django.shortcuts import render
from .forms import DenunciaForm
from Persona.models import Persona
from Denuncia.models import Denuncia
from django.http import HttpResponseRedirect


# Create your views here.

def denunciar(request):
    if request.POST:
        print(request.POST)

        comuna = request.POST.get('comuna')
        direccion = request.POST.get('direccion')
        tipo = request.POST.get('tipo')
        sexo = request.POST.get('sexo')
        color = request.POST.get('color')
        herido = request.POST.get('herido')

        if request.user.is_authenticated:
            print("Logged in")
            print(request.user.id)

            person = Persona.objects.get(usuario_id=request.user.id)
            denunciar_obj = Denuncia(comuna=comuna, direccion=direccion, tipo=tipo, sexo=sexo, color=color,
                                     herido=herido, persona=person)
        else:
            denunciar_obj = Denuncia(comuna=comuna, direccion=direccion, tipo=tipo, sexo=sexo, color=color,
                                     herido=herido)

        denunciar_obj.save()

        return HttpResponseRedirect('/')
    else:
        form = DenunciaForm()
        return render(request, 'denuncia.html', {'form': form})
