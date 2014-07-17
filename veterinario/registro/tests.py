# -*- coding: utf-8 -*-
from django.test import TestCase
from registro.models import Gato, Doutor, FactoryTratador

# Create your tests here.


class SiteServiceRequestItemFormTestCase(TestCase):

    def test_doutor_joao_trata_todos_os_gatos(self):
    	gato = Gato()
    	f = FactoryTratador()

    	doutor = Doutor(nome=u'João')

    	self.assertEqual(doutor.nome, f.getTratador(gato).nome)