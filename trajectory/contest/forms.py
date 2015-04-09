from django import forms
from .models import ContestItem, ContestItemRank


class ContestItemForm(forms.ModelForm):

    class Meta:
        model = ContestItem
        fields = [
            'route',
            'organization',
            'city',
            'authors',
            'email',
            'telephone',
            'url',
            'description',
        ]


class ContestItemRankForm(forms.ModelForm):

    class Meta:
        model = ContestItemRank
        fields = [
            'user',
            'user_rank',
            'user_comment',
        ]