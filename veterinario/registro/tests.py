# -*- coding: utf-8 -*-
import datetime

from django.test import TestCase
from .forms import AnimalForm
from .forms import VacinadaForm
from .models import Animal
from .models import Doutor
from .models import Vacina
from .models import Vacinada


class TestAnimalForm(TestCase):

    def setUp(self):
        self.data = {
            'tipo': 'DO',
            'nome':'Ruffus',
            'data_nascimento': '2013-01-01',
        }


    def test_idade_animal(self):
        animal = AnimalForm(self.data)
        self.assertTrue(animal.is_valid(), animal.errors)
        self.assertEqual(animal.instance.idade(), 1) 


    def test_form_is_valid(self):
        data = {
            'tipo': 'DO',
            'nome':'Ruffus',
            'data_nascimento': '2013-01-01',
        }
        animal = AnimalForm(self.data)
        self.assertTrue(animal.is_valid())

    def test_form_is_invalid_by_nome(self):
        self.data['nome'] = None
        animal = AnimalForm(self.data)
        self.assertFalse(animal.is_valid())

    def test_form_is_valid_by_idade(self):
        self.data['data_nascimento'] = None
        animal = AnimalForm(self.data)
        self.assertTrue(animal.is_valid(), animal.errors)


class VacinadaTestCase(TestCase):
    def setUp(self):
        self.vacina = Vacina.objects.create(nome='sarampo')
        self.animal = Animal.objects.create(tipo='DO', nome='rex')
        self.doutor = Doutor.objects.create(nome="Joao")
        self.doutor.animais.add(self.animal)
        self.vacinada_form = VacinadaForm(data={
                                          'vacina': self.vacina.id,
                                          'animal': self.animal.id,
                                          'doutor': self.doutor.id})

    def test_nao_vacinado(self):
        self.assertTrue(self.vacinada_form.is_valid())

    def test_vacinada_periodo_invalido(self):
        dois_meses = datetime.date.today() - datetime.timedelta(days=60)
        vacinada = Vacinada.objects.create(vacina=self.vacina,
                                           animal=self.animal,
                                           data=dois_meses,
                                           doutor=self.doutor)

        self.assertFalse(self.vacinada_form.is_valid())

    def test_vacinada_periodo_valido(self):
        dois_meses = datetime.date.today() - datetime.timedelta(days=120)
        vacinada = Vacinada.objects.create(vacina=self.vacina,
                                           animal=self.animal,
                                           data=dois_meses,
                                           doutor=self.doutor)

        self.assertTrue(self.vacinada_form.is_valid())


class DoutorAnimalTest(TestCase):

    def test_doutor_carlos_trata_cachorro(self):
        c01 = Animal.objects.create(tipo="CA", nome="Miau")
        c02 = Animal.objects.create(tipo="DO", nome="Auau")

        d = Doutor.objects.create(nome='Carlos')
        d.animais.add(c01)
        d.animais.add(c02)

        for animal in d.animais.all():
            if animal.tipo == 'DO':
                self.assertTrue(d.nome == 'Carlos')
