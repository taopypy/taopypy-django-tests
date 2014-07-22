from django.test import TestCase
from django import forms
from registro.forms import AnimalForm


# Create your tests here.
class TestAnimalForm(TestCase):

    def test_animal_cachorro_tem_que_passar(self):
        animal = {
            'tipo': 1,
            'nome': 'test_1',
            'idade': '10',
            'codigo': 'abc123'
        }
        animal_form = AnimalForm(data=animal)
        self.assertTrue(animal_form.is_valid())

    def test_animal_gato_tem_que_passar(self):
        animal = {
            'tipo': 2,
            'nome': 'test_2',
            'idade': '10',
            'codigo': 'abc123'
        }
        animal_form = AnimalForm(data=animal)
        self.assertTrue(animal_form.is_valid())

    def test_animal_nao_cachorro_ou_gato_deve_gerar_erro(self):
        animal = {
            'tipo': 3,
            'nome': 'test_3',
            'idade': '10',
            'codigo': 'abc123'
        }
        animal_form = AnimalForm(data=animal)
        self.assertFalse(animal_form.is_valid())
