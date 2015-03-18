from django.contrib import admin
from .models import UserFile


class UserFileAdmin(admin.ModelAdmin):
    list_display = ('name', 'date')

admin.site.register(UserFile, UserFileAdmin)
