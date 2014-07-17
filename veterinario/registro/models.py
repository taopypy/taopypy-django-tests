# -*- coding: utf-8 -*-

from django.db import models
import uuid

ANIMALS = (('DO', 'Dog'), ('CA', 'Cat'))


class Animal(models.Model):
    tipo = models.CharField(max_length=2, choices=ANIMALS)
    nome = models.CharField(max_length=50)
    idade = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50, unique=True, null=True, blank=True)

    def __unicode__(self):
        return self.nome

    def save(self, *args, **kwargs):
        self.codigo = uuid.uuid1()
        super(Animal, self).save(*args, **kwargs)

    def falar(self):
        pass


class Gato(Animal):

    def __unicode__(self):
        return self.nome

    def falar(self):
        print "%s disse: Miau!" % self.nome
        return "%s disse: Miau!" % self.nome


class Vacina(models.Model):
    animal = models.ForeignKey(Animal)
    data = models.DateField(auto_now=True)
    tipo = models.CharField(max_length=50)
    doutor = models.CharField(max_length=50)

    def __unicode__(self):
        return self.tipo


class Doutor(models.Model):
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    animais = models.ManyToManyField(Animal)

    def __unicode__(self):
        return 'Doutor %s' % self.nome


class FactoryTratador(object):
    def getTratador(self, animal):
        if animal.__class__ is Gato:
            return Doutor(nome=u"João")
