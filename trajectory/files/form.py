from django.forms import ModelForm
from .models import UserFile


class UserFileForm(ModelForm):
    class Meta:
        model = UserFile