from django import forms
from .models import ContestItemRank


class ContestItemForm(forms.Form):

    ROUTES = (
        ('01', 'Лучший электронный курс'),
        ('02', 'Лучшее визуальное оформление курса'),
        ('03', 'Лучшая инновация в контроле знаний'),
    )

    route = forms.ChoiceField(widget=forms.RadioSelect, choices=ROUTES, label="Направление")
    organization = forms.CharField(label="Организация")
    city = forms.CharField(label="Город")
    authors = forms.CharField(label="Авторы")
    email = forms.EmailField(label="Электронная почта")
    telephone = forms.CharField(label="Телефон")
    url = forms.CharField(label="Адрес ресурса")
    account = forms.CharField(label="Реквизиты доступа")
    description = forms.CharField(label="Описание основных идей", widget=forms.Textarea)


class ContestItemRankForm(forms.ModelForm):

    class Meta:
        model = ContestItemRank
        fields = [
            'user_rank',
            'user_comment',
        ]