from django.db import models
import hashlib
from os import urandom


#from ..traectory.models import Program

def key():

    key = hashlib.md5(urandom(128)).hexdigest()
    return key


class Event(models.Model):
    id = models.CharField(max_length=32, primary_key=True, default='None')
    name = models.CharField("Имя", max_length=1024)
    comment = models.TextField("Описание", max_length=4096)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    #program = models.ForeignKey(Program)

    def __str__(self):
        return self.name

    def save(self):
        if self.id == 'None':
            self.id = key()
        super(Event, self).save()