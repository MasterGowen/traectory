from django.db import models

#from ..traectory.models import Program


class Event(models.Model):
    name = models.CharField("Имя", max_length=1024)
    comment = models.TextField("Описание", max_length=4096)
    startdate = models.DateTimeField()
    enddate = models.DateTimeField()
    #program = models.ForeignKey(Program)

    def __str__(self):
        return self.name