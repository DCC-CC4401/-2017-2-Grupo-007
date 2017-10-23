from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def onghome(request):
   return render(request, 'ong.html', {})