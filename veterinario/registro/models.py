# -*- coding: utf-8 -*-
import datetime
from django.db import models

ANIMALS = (('DO', 'Dog'), ('CA', 'Cat'))


class Animal(models.Model):
    """
    Stores a single blog entry, related to :model:`blog.Blog` and
    :model:`auth.User`.

    """
    tipo = models.CharField(max_length=2, choices=ANIMALS)
    nome = models.CharField(max_length=50)
    data_nascimento = models.DateField(null=True, blank=True)

    def idade(self):
        if not self.data_nascimento:
            return 0
        return datetime.date.today().year - self.data_nascimento.year


    def __unicode__(self):
        return self.nome


class Vacina(models.Model):
    nome = models.CharField(max_length=255)

    def __unicode__(self):
        return self.name


class Doutor(models.Model):
    nome = models.CharField(max_length=50)
    animais = models.ManyToManyField(Animal)

    def __unicode__(self):
        return 'Doutor %s' % self.nome


class Vacinada(models.Model):
    vacina = models.ForeignKey(Vacina)
    animal = models.ForeignKey(Animal)
    data = models.DateTimeField(default=datetime.datetime.now(), blank=True, null=True)
    doutor = models.ForeignKey(Doutor)

    def __unicode__(self):
        return self.data
