from django.views.generic.list import ListView

from .models import Program


class ProgramListView(ListView):
    model = Program
