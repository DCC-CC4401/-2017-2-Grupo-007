from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import UserCreationForm
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from Persona.models import Persona
from Municipalidad.models import Municipalidad
from ONG.models import ONG
from Persona.forms import PersonRegisterForm
from Municipalidad.forms import MunicipalidadRegisterForm
from ONG.forms import ONGRegisterForm


def home(request):
    if request.POST:
        print(request.POST)

        username = request.POST.get('username')
        password = request.POST.get('pass')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            print("Logged in")
            print(user)
            print(user.groups.all())

            group = user.groups.all()[0].name

            print(group)

            if group == "Administrador" or group == "Persona":

                persona = Persona.objects.get(usuario_id=user.id)

                return render(request, 'Landing.html', {'persona': persona})

            if group == "Municipalidad":

                mun = Municipalidad.objects.get(usuario_id=user.id)

                return HttpResponseRedirect(reverse('municipalidad:muni'))

            if group == "ONG":

                ong = ONG.objects.get(usuario_id=user.id)

                return HttpResponseRedirect('/')  ## TODO: implementar ONG

        else:
            return render(request, 'Landing.html', {'error': "Nombre de usuario o cotraseña invalidos"})

    else:
        logout(request)
        return render(request, 'Landing.html', {})


def signup(request):
    if request.POST:
        print(request.POST)

    else:

        form_persona = PersonRegisterForm()
        form_muni = MunicipalidadRegisterForm()
        form_ong = ONGRegisterForm()

        return render(request, 'signup.html', {'person': form_persona, 'muni': form_muni, 'ong': form_ong})
