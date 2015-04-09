from django import forms
from .models import ContestItem, ContestItemRank


class ContestItemForm(forms.ModelForm):

    ROUTES = (
        ('01', 'Лучший электронный курс'),
        ('02', 'Лучшее визуальное оформление курса'),
        ('03', 'Лучшая инновация в контроле знаний'),
    )

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