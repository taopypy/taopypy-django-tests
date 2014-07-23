# -*- coding: utf-8 -*-
import datetime
from django.db import models
import uuid

ANIMALS = (('DO', 'Dog'), ('CA', 'Cat'))


class Animal(models.Model):
    """
    Stores a single blog entry, related to :model:`blog.Blog` and
    :model:`auth.User`.

    """
    tipo = models.CharField(max_length=1, choices=ANIMALS)
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
    nome = models.CharField(max_length=255)
    tipo = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class Doutor(models.Model):
    nome = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    animais = models.ManyToManyField(Animal)  # add through and explain

    def __unicode__(self):
        return 'Doutor %s' % self.nome

    def tratarAnimal(self, animal):
        primeiro_char_codigo_animal = animal.codigo[0]
        for nome_doutor, _id in self.restricao_doutor_e_animal_id:
            if self.nome == nome_doutor:
                if primeiro_char_codigo_animal != _id:
                    raise Exception(u"Animais tratados com %s devem ter número de registro iniciando em %s" % (self.nome, _id))


class Vacinada(models.Model):
    vacina = models.ForeignKey(Vacina)
    animal = models.ForeignKey(Animal)
    data = models.DateTimeField(default=datetime.datetime.now(), blank=True, null=True)
    doutor = models.ForeignKey(Doutor)

    def __unicode__(self):
        return self.data


class FactoryTratador(object):
    def getTratador(self, animal):
        if animal.__class__ is Gato:
            return Doutor(nome=u"João")
