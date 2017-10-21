from django.shortcuts import render

def ficha(request):
    return render(request, 'fichaAnimal.html', {})