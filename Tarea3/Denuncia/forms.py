from django import forms

from .models import Denuncia
from utils.choices import tipoAnimal, sexoChoice, colorChoice, heridoChoice, comunaChoice


class DenunciaForm(forms.Form):
    comuna = forms.ChoiceField(choices=comunaChoice)
    direccion = forms.CharField(max_length=50)
    tipo = forms.ChoiceField(choices=tipoAnimal)
    sexo = forms.ChoiceField(choices=sexoChoice)
    color = forms.ChoiceField(choices=colorChoice)
    herido = forms.ChoiceField(choices=heridoChoice)