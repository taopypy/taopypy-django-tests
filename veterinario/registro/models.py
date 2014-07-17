from django.db import models
import uuid



class Animal(models.Model):
    nome = models.CharField(max_length=50)
    idade = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50, unique=True, null=True, blank=True)

    def __unicode__(self):
        return self.nome

    def save(self, *args, **kwargs):
        self.codigo = uuid.uuid1()
        super(Animal, self).save(*args, **kwargs)

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
        return self.nome
