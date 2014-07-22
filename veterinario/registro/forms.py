# encoding: utf-8
from django import forms
from .models import Animal
from .models import Vacina


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        exclude = ['codigo',]


class VacinaForm(forms.ModelForm):
    class Meta:
        model = Vacina
