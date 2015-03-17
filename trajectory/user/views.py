from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.core.context_processors import csrf
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.core.mail import send_mail

from .models import User
from .forms import UserForm

from ..trajectory.models import Trajectory


class UserListView(ListView):
    model = User

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now
        return context


class UserCreate(CreateView):  # TODO: DEPRECATED
    model = User

    success_url = '/users/'


def new_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()  # TODO:  сгенерить линк и отправить юзеру

            trajectory = Trajectory()
            trajectory.user_id = user.id
            trajectory.save()

            link = 'http://localhost:8000/traj/' + trajectory.id
            #send_mail('NOTV2015', link, 'admin@openedu.urfu.ru', [user.email])

            return redirect(link)# render(request, 'trajectory/new.html', {"user": user.id, "trajectory": trajectory.id, "link": link})
    args = {}
    args.update(csrf(request))
    args['form'] = UserForm()
    return render(request, 'user/user_form.html', args)