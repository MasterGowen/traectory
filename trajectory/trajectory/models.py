import hashlib
from os import urandom

from django.db import models

from ..event.models import Event


def key():

    key = hashlib.md5(urandom(128)).hexdigest()
    return key


class Trajectory(models.Model):
    id = models.CharField(max_length=32, primary_key=True, default='None')
    comment = models.TextField(max_length=22048, blank=True, null=True)
    user_id = models.CharField(max_length=32, default='None')

    def save(self):
        if self.id == 'None':
            self.id = key()
        super(Trajectory, self).save()


class Cell(models.Model):
    id = models.CharField(max_length=32, primary_key=True, default='None')
    name = models.CharField('Название', max_length=1024, default='Ячейка')
    events = models.ManyToManyField(Event)

    def __str__(self):
        return self.name

    def save(self):
        if self.id == 'None':
            self.id = key()
        super(Cell, self).save()


class Program(models.Model):
    id = models.CharField(max_length=32, primary_key=True, default='None')
    name = models.CharField('Название', max_length=1024, blank=True, null=True)
    comment = models.TextField('Описание', max_length=4096, blank=True, null=True)
    payd = models.BooleanField('Платно', default=False)
    cells = models.ManyToManyField(Cell)

    def __str__(self):
        return self.name

    def save(self):
        if self.id == 'None':
            self.id = key()
        super(Program, self).save()
