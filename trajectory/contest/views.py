from django.shortcuts import render, redirect
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView

from django.http import HttpResponse

from .models import ContestItem, ContestItemRank
from .forms import ContestItemForm, ContestItemRankForm

# CRUD


def create_contest_item(request):
    if request.method == 'POST':
        form = ContestItemForm(request.POST)
        if form.is_valid():
            contest_item = form.save(commit=False)
            contest_item.save()

            return render(request, 'contest/thanks.html')
        else:
            return HttpResponse('Invalid form')
    args = {}
    args.update(csrf(request))
    args['form'] = ContestItemForm()
    return render(request, 'contest/contest.html', args)


def read_contest_item_all(request):
    contest_items = ContestItem.objects.all()
    return render(request, 'contest/contest_list.html', {
        "contest_items": contest_items
    })


def read_contest_item(request, pk):
    contest_item = get_object_or_404(ContestItem, pk=pk)
    return render(request, 'contest/contest_item.html', {
        'contest_item': contest_item,
    })


def update_contest_item(request, id):
    pass


def delete_contest_item(request, id):
    pass


@login_required()
def create_contest_item_rank(request):

    if request.method == 'POST':
        form = ContestItemRankForm(request.POST)
        if form.is_valid():
            contest_item_rank = form.save(commit=False)
            contest_item_rank.save()

            contest_item_rank.user = User.objects.get(pr=request.user.id)
            contest_item_rank.save()
            return redirect('http://notv.urfu.ru/')