# encoding: utf-8
from django import forms
from .models import Animal


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        exclude = ['codigo',]

