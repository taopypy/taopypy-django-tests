# -*- coding: utf-8 -*-
import datetime

from django.test import TestCase
from .forms import AnimalForm
from .forms import VacinadaForm
from .models import Animal
from .models import Gato
from .models import Doutor
from .models import FactoryTratador
from .models import Vacina
from .models import Vacinada


class TestAnimalForm(TestCase):

    def test_form_is_valid(self):
        data = {
            'tipo': 'DO',
            'nome':'Ruffus',
            'idade':10,
        }
        animal = AnimalForm(data)
        self.assertTrue(animal.is_valid())

    def test_form_is_invalid_by_nome(self):
        data = {
            'tipo': 'DO',
            'nome':None,
            'idade':12,
        }

        animal = AnimalForm(data)
        self.assertFalse(animal.is_valid())

    def test_form_is_invalid_by_idade(self):
        data = {
            'tipo': 'DO',
            'nome':'Ruffus',
            'idade':None,
        }
        animal = AnimalForm(data)
        self.assertFalse(animal.is_valid())

    def test_form_create_code(self):
        data = {
            'tipo': 'DO',
            'nome':'Ruffus',
            'idade':12,
        }

        animal = AnimalForm(data)
        animal.is_valid()
        animal.save()

        myanimal = Animal.objects.get(id=animal.instance.id)
        self.assertTrue(myanimal.codigo)

    def test_form_create_unique_code(self):

        data = {
            'tipo': 'DO',
            'nome':'Ruffus',
            'idade':12,
        }

        animal = AnimalForm(data)
        animal.is_valid()
        animal.save()

        myanimal = Animal.objects.get(id=animal.instance.id)
        self.assertTrue(myanimal.codigo)

        data = {
            'tipo': 'DO',
            'nome':'Ruffus',
            'idade':12,
        }

        animal2 = AnimalForm(data)
        animal2.is_valid()
        animal2.save()

        myanimal2 = Animal.objects.get(id=animal2.instance.id)
        self.assertTrue(myanimal2.codigo)

        self.assertNotEqual(myanimal.codigo, myanimal2.codigo)


class VacinadaTestCase(TestCase):
    def setUp(self):
        self.vacina = Vacina.objects.create(nome='sarampo', tipo='tipo01')
        self.animal = Animal.objects.create(tipo='DO', nome='rex', idade='01', codigo='001')
        self.doutor = Doutor.objects.create(nome="Joao", tipo="VET")
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

class SiteServiceRequestItemFormTestCase(TestCase):

    def test_doutor_joao_trata_todos_os_gatos(self):
    	gato = Gato()
    	f = FactoryTratador()

    	doutor = Doutor(nome=u'João')

    	self.assertEqual(doutor.nome, f.getTratador(gato).nome)


class DoutorAnimalTest(TestCase):

    def create_doutor(self, nome="Joao", tipo="veterinario"):
        return Doutor.objects.create(nome=nome, tipo=tipo)

    def create_animal(self, tipo="CA", nome="Rex", idade=1, codigo="001"):
        return Animal.objects.create(tipo=tipo, nome=nome, idade=idade, codigo=codigo)

    def test_doutor_carlos_trata_cachorro(self):
        c01 = self.create_animal(tipo="CA", nome="Miau", idade=1, codigo="001")
        c02 = self.create_animal(tipo="DO", nome="Auau", idade=2, codigo="002")

        d = self.create_doutor(nome="Carlos", tipo="veterinario")
        d.animais.add(c01)
        d.animais.add(c02)

        for animal in d.animais.all():
            if animal.tipo == 'DO':
                self.assertTrue(d.nome == 'Carlos')
