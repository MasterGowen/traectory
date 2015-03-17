from django.views.generic.list import ListView
from django.shortcuts import render

from .models import Program, Trajectory, Event
from ..user.models import User


class ProgramListView(ListView):
    model = Program


def trajectory(request, pk):
    return render(request, 'trajectory/new.html')