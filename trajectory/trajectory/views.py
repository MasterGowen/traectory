import json

from django.views.generic.list import ListView
from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.core.exceptions import ObjectDoesNotExist

from .models import Program, Trajectory, Cell
from ..user.models import User
from ..event.models import Event


class ProgramListView(ListView):
    model = Program


def trajectory_view(request, pk):
    programs = Program.objects.all()
    trajectory = Trajectory.objects.get(pk=pk)
    user = User.objects.get(pk=trajectory.user_id)
    return render(request, 'trajectory/program_list.html',
                  {
                      'user': user,
                      'programs': programs
                  })


@require_POST
def trajectory_save(request):
    trajectory_id = request.META['HTTP_REFERER'].split('/')[-2]
    trajectory = Trajectory.objects.get(pk=trajectory_id)

    trajectory.events.clear()


    data = request.POST.copy()
    data.pop('csrfmiddlewaretoken', None)
    data.pop('submit', None)

    cells_ids = []

    for item in data:
        cells_ids.append(item)
        event_id = data[item]
        try:
            user_event = Event.objects.get(pk=event_id)
        except ObjectDoesNotExist:
            user_event = 'None'
        if user_event:
            trajectory.events.add(user_event)

    cells = Cell.objects.filter(pk__in=cells_ids)

    for cell in cells:
        program_id = cell.program_set.all()

    programs = Program.objects.filter(pk__in=program_id)

    trajectory.comment = json.dumps(data)
    trajectory.save()

    user = User.objects.get(pk=trajectory.user_id)

    return render(request, 'trajectory/trajectory.html', {
        'user': user,
        'trajectory': trajectory,
        'cells': cells,
        'programs': programs
    })
