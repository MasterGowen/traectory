import hashlib
from os import urandom
from django.db import models


def key():
    return hashlib.md5(urandom(128)).hexdigest()[:16]


class Event(models.Model):
    id = models.CharField(max_length=16, primary_key=True, default='None')
    name = models.CharField("Имя", max_length=1024)
    comment = models.TextField("Описание", max_length=4096, blank=True, null=True)
    startdate = models.DateTimeField(blank=True, null=True)
    enddate = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(verbose_name='Image', upload_to='images/%Y/%m', blank=True)

    def __str__(self):
        return self.name

    def save(self):
        if self.id == 'None':
            self.id = key()
        super(Event, self).save()