from django.views.generic.list import ListView
from django.shortcuts import render

from .models import Program, Trajectory
from ..user.models import User


class ProgramListView(ListView):
    model = Program


def trajectoryView(request, pk):
    trajectory = Trajectory.objects.get(pk=pk)
    user = User.objects.get(pk=trajectory.user_id)
    return render(request, 'trajectory/program_list.html', {'user': user})