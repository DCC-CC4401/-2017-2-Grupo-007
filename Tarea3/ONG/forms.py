from django import forms
from django.contrib.auth import login
from django.contrib.auth.models import Group, User
from ONG.models import ONG
from django.core.files.storage import FileSystemStorage


class ONGRegisterForm(forms.Form):
    tipo = forms.CharField(widget=forms.HiddenInput(), initial='ONG')
    nombre = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    username = forms.CharField(label='Nombre de usuario', widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput(attrs={'class': 'form-control'}), required=True)
    ubicacion = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}), required=True)
    foto = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control'}), required=True)

    def is_valid(self):
        super(ONGRegisterForm, self).is_valid()

        return self.cleaned_data['tipo'] == 'ONG'

    def save(self):
        group = Group.objects.get(name='ONG')

        user = User.objects.create_user(username=self.cleaned_data['username'], password=self.cleaned_data['password'])

        group.user_set.add(user)

        file = self.cleaned_data['foto']

        fs = FileSystemStorage()

        filename = fs.save(file.name, file)
        uploaded_file_url = fs.url(filename)

        ong = ONG(nombre=self.cleaned_data['nombre'], ubicacion=self.cleaned_data['ubicacion'], foto=self.cleaned_data['foto'], administrador=user)
        ong.save()
