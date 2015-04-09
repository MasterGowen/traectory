import hashlib
from os import urandom, path
from datetime import datetime
import uuid
import time

from django.db import models

from ..user.models import User



def key():
    return hashlib.md5(urandom(128)).hexdigest()

def generate_new_filename(instance, filename):
    f, ext = path.splitext(filename)
    filename = '%s%s' % (uuid.uuid4().hex, ext)
    fullpath = 'files/' + time.strftime('%Y/%m') + '/' + filename
    return fullpath


class UserFile(models.Model):
    id = models.CharField(max_length=32, primary_key=True, default='None')
    name = models.CharField('Название', max_length=4096)
    file = models.FileField(verbose_name='User file', upload_to=generate_new_filename)
    date = models.DateField(auto_now_add=True, default=datetime.now())
    user = models.ForeignKey(User, blank=True, null=True)

    def __str__(self):
        return self.name

    def save(self):
        if self.id == 'None':
            self.id = key()
        super(UserFile, self).save()

