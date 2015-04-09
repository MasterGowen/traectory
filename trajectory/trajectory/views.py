import json

from django.shortcuts import render
from django.views.decorators.http import require_POST
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.admin.views.decorators import staff_member_required

from .models import Program, Trajectory, Cell
from ..user.models import User
from ..event.models import Event
from ..files.models import UserFile


def trajectory_view(request, pk):
    programs = Program.objects.all()
    trajectory = Trajectory.objects.get(pk=pk)
    user = User.objects.get(pk=trajectory.user_id)
    active_events = []
    for event in trajectory.events.all():
        active_events.append(event.id)
    return render(request, 'trajectory/program_list.html',
                  {
                      'user': user,
                      'programs': programs,
                      'active_events': active_events,
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


@staff_member_required
def stats(request):
    event_users = {}
    event_users_status = {}
    event_users.clear()
    event_users_status.clear()
    events = Event.objects.all()
    for event in events:
        users_ids = []
        trajectories = event.trajectory_set.all()
        for trajectory in trajectories:
            users_ids.append(trajectory.user_id)
        users = User.objects.filter(pk__in=users_ids)
        event_users[event] = users

        for user in users:
            event_users_status[event.id].append(user.status)
        event_users_status_json = json.dumps(event_users_status)

    number_users = User.objects.count()
    number_files = UserFile.objects.count()
    users = User.objects.order_by('f')

    userfiles = {}

    for user in users:
        files = UserFile.objects.filter(user=user)
        userfiles[user.id] = files

    return render(request, 'trajectory/stats.html', {
        'event_users': event_users,
        'number_users': number_users,
        'users': users,
        'userfiles': userfiles,
        'number_files': number_files,
        'event_users_status_json': event_users_status_json,
        }
    )