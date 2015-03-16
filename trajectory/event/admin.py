from django.contrib import admin

from .models import Event


class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'startdate', 'enddate', 'comment')

admin.site.register(Event, EventAdmin)
