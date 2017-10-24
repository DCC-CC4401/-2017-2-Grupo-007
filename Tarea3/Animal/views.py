from django.shortcuts import render
from Animal.models import Animal
from Persona.models import Persona
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def ficha(request, animal_id):
    try:
        person = Persona.objects.get(usuario_id=request.user.id)
    except:
        person = None
    data = Animal.objects.filter(id=animal_id)
    template = loader.get_template('fichaAnimal.html')
    context = {
        'persona': person,
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
        ult_list = Animal.objects.order_by('-fecha_ingreso')[:10]
        template = loader.get_template('ong_adopcion.html')
        context = {
            'persona': person,
            'ult_list': ult_list,
        }
        return HttpResponse(template.render(context, request))
    else:

        return HttpResponseRedirect(reverse('ong:onghome'))
