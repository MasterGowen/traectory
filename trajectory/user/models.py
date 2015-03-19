from django.db import models
from os import urandom

from ..trajectory.models import Trajectory


def key():
    return int.from_bytes(urandom(32), byteorder="little")[:32]


class User(models.Model):
    id = models.IntegerField(max_length=32, primary_key=True, default=0)
    i = models.CharField("Имя", max_length=1024)
    f = models.CharField("Фамилия", max_length=1024)
    o = models.CharField("Отчество", max_length=1024)
    city = models.CharField("Город", max_length=1024, blank=True, null=True)
    email = models.EmailField("Электронная почта", max_length=1024)
    tel = models.CharField("Телефон", max_length=1024)
    trajectories = models.ManyToManyField(Trajectory)
    link = models.CharField("Персональная ссылка", max_length=1024, blank=True, null=True)
    online = 'online'
    offline = 'offline'
    STATUS = (
        (online, 'Заочно'),
        (offline, 'Очно')
    )
    status = models.CharField("Статус", max_length=7, choices=STATUS, default=offline)
    date = models.DateField(auto_now_add=True, blank=True)

    class Meta:
        unique_together = ("email", "f")

    def save(self):
        if self.id == 0:
            self.id = key()
        super(User, self).save()
