from django.contrib import admin

from .models import Trajectory, Cell, Program


class TrajectoryAdmin(admin.ModelAdmin):
    pass


class ProgramAdmin(admin.ModelAdmin):
    filter_horizontal = ('cells',)


class CellAdmin(admin.ModelAdmin):
    filter_horizontal = ('events',)

admin.site.register(Trajectory, TrajectoryAdmin)
admin.site.register(Cell, CellAdmin)
admin.site.register(Program, ProgramAdmin)
