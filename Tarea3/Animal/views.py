from django.shortcuts import render
from Animal.models import Animal
from django.template import loader
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def ficha(request, animal_id):
    data = Animal.objects.filter(id=animal_id)
    template = loader.get_template('fichaAnimal.html')
    print(Animal.nombre)
    context = {
        'data': data
    }
    return HttpResponse(template.render(context, request))


def enadopcion(request):
    print("Aqui")
    try:
        test = request.user.groups.all()[0].name == "Persona"
    except:
        test = False

    if test:
        ult_list = Animal.objects.order_by('-fecha_ingreso')[:10]
        template = loader.get_template('ong_adopcion.html')
        context = {
            'ult_list': ult_list,
        }
        return HttpResponse(template.render(context, request))
    else:

        return HttpResponseRedirect(reverse('ong:onghome'))



