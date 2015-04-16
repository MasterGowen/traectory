from django.shortcuts import render, redirect
from django.core.context_processors import csrf
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

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
    contest_items_ranking = {}
    contest_items = ContestItem.objects.all()
    for contest_item in contest_items:
        contest_items_ranking[contest_item.id] = []
        for rank in contest_item.rank.all():
            contest_items_ranking[contest_item.id].append(rank.user.id)

    return render(request, 'contest/contest_list.html', {
        "contest_items": contest_items,
        "contest_items_ranking": contest_items_ranking,
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
def create_contest_item_rank(request, pk):

    if request.method == 'POST':
        form = ContestItemRankForm(request.POST)
        if form.is_valid():
            contest_item_rank = form.save(commit=False)
            contest_item_rank.save()

            contest_item_rank.user = User.objects.get(pk=request.user.id)
            contest_item_rank.save()

            contest_item = ContestItem.objects.get(pk=pk)
            contest_item.rank.add(contest_item_rank)
        else:
            return render(request, '500.html')
    args = {}
    args.update(csrf(request))
    args['form'] = ContestItemRankForm()
    return redirect('/contest/all/')