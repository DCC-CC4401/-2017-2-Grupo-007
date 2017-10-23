from django.shortcuts import render
from Animal.models import Animal
from django.template import loader
from django.http import HttpResponse

def ficha(request, animal_id):
    data = Animal.objects.filter(id=animal_id)
    template = loader.get_template('fichaAnimal.html')
    context = {
        'data': data
    }
    return HttpResponse(template.render(context, request))