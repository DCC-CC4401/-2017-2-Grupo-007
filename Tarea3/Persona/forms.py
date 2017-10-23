from django import forms
from utils.choices import sexoPersonaChoices
from django.contrib.auth.models import Group, User
from Persona.models import Persona


class PersonRegisterForm(forms.Form):
    tipo = forms.CharField(widget=forms.HiddenInput(), initial='Persona')
    nombre = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    username = forms.CharField(label='Nombre de usuario', widget=forms.TextInput(attrs={'class': 'form-control'}),
                               required=True)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}),
                               required=True)
    rut = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}), required=True)
    telefono = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    sexo = forms.ChoiceField(choices=sexoPersonaChoices, widget=forms.Select(attrs={'class': 'form-control'}),
                             required=True)
    foto = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}), required=True)

    def is_valid(self):
        return self.cleaned_data['tipo'] == 'Persona'

    def save(self):
        group = Group.objects.get(name='Persona')

        user = User.objects.create_user(username=self.cleaned_data['username'], password=self.cleaned_data['password'])

        group.user_set.all(user)

        person = Persona(nombre=self.cleaned_data['nombre'], rut=self.cleaned_data['rut'],
                         email=self.cleaned_data['email'], fono=self.cleaned_data['telefono'],
                         sexo=self.cleaned_data['sexo'], usuario=user)
        person.save()
