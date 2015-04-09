from django.shortcuts import render, redirect
from django.core.context_processors import csrf
from django.utils import timezone
from django.views.generic.list import ListView
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


def new_user(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()

            trajectory = Trajectory()
            trajectory.user_id = user.id
            trajectory.save()

            link = 'http://openedu.urfu.ru/notv/tr/' + trajectory.id + '/'
            user.link = link
            user.save()
            try:
                send_mail('НОТВ 2015', 'Ваша персональная ссылка:'+link, 'info@notv.urfu.ru', [user.email])
            except:
                pass
            return redirect(link)
    args = {}
    args.update(csrf(request))
    args['form'] = UserForm()
    return render(request, 'user/user_form.html', args)