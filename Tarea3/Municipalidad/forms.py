from django import forms
from django.contrib.auth import login
from django.contrib.auth.models import Group, User
from utils.choices import comunaChoice
from Municipalidad.models import Municipalidad
from utils.choices import estadoChoice
from django.core.files.storage import FileSystemStorage


class MunicipalidadRegisterForm(forms.Form):
    tipo = forms.CharField(widget=forms.HiddenInput(), initial='Municipalidad')
    nombre = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    username = forms.CharField(label='Nombre de usuario', widget=forms.TextInput(attrs={'class': 'form-control'}),
                               required=True)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               required=True)
    comuna = forms.ChoiceField(choices=comunaChoice, widget=forms.Select(attrs={'class': 'form-control'}),
                               required=True)
    direccion = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    foto = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}), required=True)

    def is_valid(self):
        super(MunicipalidadRegisterForm, self).is_valid()

        return self.cleaned_data['tipo'] == 'Municipalidad'

    def save(self):
        group = Group.objects.get(name='Municipalidad')

        user = User.objects.create_user(username=self.cleaned_data['username'], password=self.cleaned_data['password'])

        group.user_set.add(user)

        file = self.cleaned_data['foto']

        fs = FileSystemStorage()

        filename = fs.save(file.name, file)
        uploaded_file_url = fs.url(filename)

        print(uploaded_file_url)

        muni = Municipalidad(nombre=self.cleaned_data['nombre'], comuna=self.cleaned_data['comuna'],
                             direccion=self.cleaned_data['direccion'], foto=self.cleaned_data['foto'], administrador=user)
        muni.save()


class Gestionar(forms.Form):
    estado = forms.ChoiceField(widget=forms.Select(), choices=estadoChoice)
