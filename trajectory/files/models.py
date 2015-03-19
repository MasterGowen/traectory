import hashlib
from os import urandom
from datetime import datetime

from django.db import models

from ..user.models import User


def key():
    return hashlib.md5(urandom(128)).hexdigest()[:16]


class UserFile(models.Model):
    id = models.CharField(max_length=16, primary_key=True, default='None')
    name = models.CharField('Название', max_length=4096)
    file = models.FileField(verbose_name='User file', upload_to='files/%Y/%m')
    date = models.DateField(auto_now_add=True, default=datetime.now())
    user = models.ForeignKey(User, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self):
        if self.id == 'None':
            self.id = key()
        super(UserFile, self).save()

