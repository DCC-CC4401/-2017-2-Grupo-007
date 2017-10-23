from django import forms
from django.contrib.auth.models import Group, User
from utils.choices import comunaChoice
from Municipalidad.models import Municipalidad


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
        return self.cleaned_data['tipo'] == 'Municipalidad'

    def save(self):
        group = Group.objects.get(name='Municipalidad')

        user = User.objects.create_user(username=self.cleaned_data['username'], password=self.cleaned_data['password'])

        group.user_set.all(user)

        muni = Municipalidad(nombre=self.cleaned_data['nombre'], comuna=self.cleaned_data['comuna'],
                             direccion=self.cleaned_data['dierccion'], foto=self.cleaned_data['foto'], usuario=user)
        muni.save()
