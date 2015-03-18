from django.contrib import admin
from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('f', 'i', 'o')

admin.site.register(User, UserAdmin)
