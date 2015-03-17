import json

from django.views.generic.list import ListView
from django.shortcuts import render
from django.views.decorators.http import require_POST

from .models import Program, Trajectory
from ..user.models import User


class ProgramListView(ListView):
    model = Program


def trajectory_view(request, pk):
    trajectory = Trajectory.objects.get(pk=pk)
    user = User.objects.get(pk=trajectory.user_id)
    return render(request, 'trajectory/program_list.html', {'user': user})


@require_POST
def trajectory_save(request):
    trajectory_id = request.META['HTTP_REFERER'].split('/')[-2]
    trajectory = Trajectory.objects.get(pk=trajectory_id)

    data = json.loads(request.body)

    user = User.objects.get(pk=trajectory.user_id)

    unicode()
