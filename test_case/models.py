from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from random import randint
from datetime import date


def random_integer():
    return randint(1, 100)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birthday = models.DateField(default=date(1900, 1, 1))
    number = models.IntegerField(default=random_integer)

    def __str__(self):
        return f'{self.user.username} Profile'
