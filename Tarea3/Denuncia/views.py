from django.shortcuts import render
from .forms import DenunciaForm


# Create your views here.

def denunciar(request):
    form = DenunciaForm()
    return render(request, 'denuncia.html', {'form': form})
