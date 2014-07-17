# encoding: utf-8
from django.test import TestCase
from .forms import AnimalForm
from .models import Animal


class TestAnimalForm(TestCase):

    def test_form_is_valid(self):
        data = {
            'nome':'Ruffus',
            'idade':10,
        }
        animal = AnimalForm(data)
        self.assertTrue(animal.is_valid())

    def test_form_is_invalid_by_nome(self):
        data = {
        'nome':None,
        'idade':12,
        }

        animal = AnimalForm(data)
        self.assertFalse(animal.is_valid())

    def test_form_is_invalid_by_idade(self):
        data = {
        'nome':'Ruffus',
        'idade':None,
        }
        animal = AnimalForm(data)
        self.assertFalse(animal.is_valid())

    def test_form_create_code(self):
        data = {
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
        'nome':'Ruffus',
        'idade':12,
        }

        animal = AnimalForm(data)
        animal.is_valid()
        animal.save()

        myanimal = Animal.objects.get(id=animal.instance.id)
        self.assertTrue(myanimal.codigo)

        data = {
        'nome':'Ruffus',
        'idade':12,
        }

        animal2 = AnimalForm(data)
        animal2.is_valid()
        animal2.save()

        myanimal2 = Animal.objects.get(id=animal2.instance.id)
        self.assertTrue(myanimal2.codigo)

        self.assertNotEqual(myanimal.codigo, myanimal2.codigo)
