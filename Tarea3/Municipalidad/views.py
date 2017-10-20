from django.shortcuts import render

# Create your views here.
def municipalidades(request):
    return render(request, 'muni.html', {})