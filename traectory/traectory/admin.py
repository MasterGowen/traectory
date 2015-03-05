from django.contrib import admin

from .models import Traectory, Cell, Program


class TraectoryAdmin(admin.ModelAdmin):
    pass


class ProgramAdmin(admin.ModelAdmin):
    filter_horizontal = ('cells',)


class CellAdmin(admin.ModelAdmin):
    filter_horizontal = ('events',)

admin.site.register(Traectory, TraectoryAdmin)
admin.site.register(Cell, CellAdmin)
admin.site.register(Program, ProgramAdmin)
