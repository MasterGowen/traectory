from django.views.generic.list import ListView
from django.shortcuts import render

from .models import Program, Trajectory, Event
from ..user.models import User


class ProgramListView(ListView):
    model = Program


def trajectoryView(request, pk):
    trajectory = Trajectory.objects.get(pk=pk)
    user = User.objects.get(pk=trajectory.user_id)
    return render(request, 'trajectory/trajectory.html', {'user': user})