# -*- coding: utf-8 -*-
from django.test import TestCase
from registro.models import Gato, Doutor, FactoryTratador
from registro.models import Animal


# Create your tests here.
class SiteServiceRequestItemFormTestCase(TestCase):

    def test_doutor_joao_trata_todos_os_gatos(self):
    	gato = Gato()
    	f = FactoryTratador()

    	doutor = Doutor(nome=u'João')

    	self.assertEqual(doutor.nome, f.getTratador(gato).nome)


# Testing the models
class DoutorAnimalTest(TestCase):

    def create_doutor(self, nome="Joao", tipo="veterinario"):
        return Doutor.objects.create(nome=nome, tipo=tipo)

    def create_animal(self, tipo="CA", nome="Rex", idade=1, codigo="001"):
        return Animal.objects.create(tipo=tipo, nome=nome, idade=idade, codigo=codigo)

    def test_doutor_creation(self):
        d = self.create_doutor()
        self.assertTrue(isinstance(d, Doutor))
        self.assertEqual(d.__unicode__(), d.nome)

    def test_animal_creation(self):
        a = self.create_animal()
        self.assertTrue(isinstance(a, Animal))
        self.assertEqual(a.__unicode__(), a.nome)

    def test_doutor_carlos_trata_cachorro(self):
        c01 = self.create_animal(tipo="CA", nome="Miau", idade=1, codigo="001")
        c02 = self.create_animal(tipo="DO", nome="Auau", idade=2, codigo="002")

        d = self.create_doutor(nome="Carlos", tipo="veterinario")
        d.animais.add(c01)
        d.animais.add(c02)

        for animal in d.animais.all():
            if animal.tipo == 'DO':
                self.assertTrue(d.nome == 'Carlos')


