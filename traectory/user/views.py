from django.shortcuts import render
from django.utils import timezone
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from .models import User


class UserListView(ListView):
    model = User

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now
        return context


class UserCreate(CreateView):
    model = User

    success_url = '/users/'

