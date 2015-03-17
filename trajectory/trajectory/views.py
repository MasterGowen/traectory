import json

from django.http import HttpResponse
from django.views.generic.list import ListView
from django.shortcuts import render
from django.views.decorators.http import require_POST

from .models import Program, Trajectory
from ..user.models import User


class ProgramListView(ListView):
    model = Program


def trajectory_view(request, pk):
    programs = Program.objects.all()
    trajectory = Trajectory.objects.get(pk=pk)
    user = User.objects.get(pk=trajectory.user_id)
    return render(request, 'trajectory/program_list.html', {'user': user, 'programs': programs})


@require_POST
def trajectory_save(request):
    trajectory_id = request.META['HTTP_REFERER'].split('/')[-2]
    trajectory = Trajectory.objects.get(pk=trajectory_id)


    data = request.POST.copy()
    data.pop('csrfmiddlewaretoken', None)
    data.pop('submit', None)
    trajectory.comment = json.dumps(data)
    trajectory.save()

    user = User.objects.get(pk=trajectory.user_id)

    return HttpResponse(json.dumps(data), content_type='application/json')
