from django.shortcuts import render
from django.core.context_processors import csrf
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

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
            user.save()  # TODO: Создать траекторию заранее, выдать её id в реквест, сгенерить линк и отправить юзеру

            trajectory = Trajectory()
            trajectory.save()
            return render(request, 'trajectory/new.html', {"user": user.id, 'trajectory': trajectory.id})
    args = {}
    args.update(csrf(request))
    args['form'] = UserForm()
    return render(request, 'user/user_form.html', args)