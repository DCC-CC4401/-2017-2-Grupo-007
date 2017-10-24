from django.shortcuts import render
from Animal.models import Animal
from Persona.models import Persona
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect


def ficha(request, animal_id):
    data = Animal.objects.filter(id=animal_id)
    template = loader.get_template('fichaAnimal.html')
    context = {
        'data': data
    }
    return HttpResponse(template.render(context, request))


def enadopcion(request):
    try:
        test = request.user.groups.all()[0].name == "Persona"
        person = Persona.objects.get(usuario_id=request.user.id)
    except:
        test = False
        person = None

    if test:
        ult_list = Animal.objects.order_by('-fecha_ingreso')[:5]
        template = loader.get_template('ong_adopcion.html')
        context = {
            'persona': person,
            'ult_list': ult_list,
        }
        print(context)
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponseRedirect('/')
