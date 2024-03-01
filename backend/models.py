from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.db import models


class Department(models.Model):          # Отдел пользователя
    name = name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Отдел'
        verbose_name_plural = "Список отделов"
        ordering = ('name',)

    def __str__(self):
        return str(self.name)

class Team(models.Model): #Команды
    name = models.CharField(max_length=50)


class User(models.Model):               # Пользователи
    name = models.CharField(max_length=50)
    team = models.ForeignKey(Team, verbose_name='Команда', related_name='user', null=True, blank=True,on_delete=models.SET_NULL)
    department = models.ForeignKey(Department, verbose_name='Отдел', null=True,
                      related_name='user', blank=True,
                      on_delete=models.SET_NULL)

    def __str__(self):
        return self.name



class Tournament(models.Model):        # Турниры
    name = models.CharField(max_length=50)



class Game(models.Model): # Матчи
    name = models.CharField(max_length=50)


