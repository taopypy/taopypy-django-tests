# encoding: utf-8
import datetime
from django import forms
from .models import Animal
from .models import Vacina
from .models import Vacinada


class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        exclude = ['codigo',]


class VacinaForm(forms.ModelForm):
    class Meta:
        model = Vacina

class VacinadaForm(forms.ModelForm):
    class Meta:
        model = Vacinada
        excludes = ['data']

    def clean(self):
        animal = self.cleaned_data['animal']
        ultima_vacina = Vacinada.objects.filter(animal=animal)
        if not ultima_vacina.exists():
            return self.cleaned_data
        tres_meses = datetime.datetime.now() - datetime.timedelta(days=90)
        ultima_vacina = ultima_vacina.latest('data').data
        if ultima_vacina.date() >= tres_meses.date():
            raise forms.ValidationError('Seu animal ja foi vacinado')
        return self.cleaned_data
