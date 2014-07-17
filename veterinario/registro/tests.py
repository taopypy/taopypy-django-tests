# -*- coding: utf-8 -*-
from django.test import TestCase
from .forms import AnimalForm
from .models import Animal
from .models import Gato
from .models import Doutor
from .models import FactoryTratador


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
