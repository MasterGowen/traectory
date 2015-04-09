from django.db import models
from django.contrib.auth.models import User


class ContestItemRank(models.Model):
    user = models.ForeignKey(User)
    user_rank = models.IntegerField(
        "Оценка",
        max_length=8,
        blank=True,
        null=True
    )

    user_comment = models.CharField(
        "Комментарий",
        max_length=4096,
        blank=True,
        null=True
    )


class ContestItem(models.Model):

    ROUTES = (
        ('01', 'Лучший электронный курс'),
        ('02', 'Лучшее визуальное оформление курса'),
        ('03', 'Лучшая инновация в контроле знаний'),
    )

    route = models.CharField(
        "Номинация",
        max_length=2,
        choices=ROUTES
    )
    organization = models.CharField(
        "Организация",
        max_length=1024
    )
    city = models.CharField(
        "Город",
        max_length=1024
    )
    authors = models.CharField(
        "Авторы",
        max_length=1024
    )
    email = models.EmailField(
        "Электронная почта",
        max_length=1024
    )
    telephone = models.CharField(
        "Контактный телефон",
        max_length=1024
    )
    url = models.URLField(
        "Адрес ресурса",
        max_length=1024,
        blank=True,
        null=True
    )

    account = models.CharField(
        "Реквизиты доступа",
        max_length=1024,
        blank=True,
        null=True
    )

    description = models.CharField(
        "Описание основных идей",
        max_length=4096
    )

    rank = models.ManyToManyField(ContestItemRank)

    summary_rank = models.IntegerField(
        "Общая оценка",
        max_length=8,
        null=True,
        blank=True
    )
