from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
    name_project = models.CharField('Название проекта', max_length=128, unique=True)
    users_project = models.ManyToManyField(User)

    def __str__(self):
        return f'Проект {self.name_project}'

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Todo(models.Model):
    todo_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    todo_user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo_text = models.CharField('Текст заметки', max_length=200)
    todo_date_create = models.DateTimeField('Время создания заметки')
    todo_date_update = models.DateTimeField('Время изменения заметки')
    todo_open_close = models.BooleanField('Открыта или зактыта ToDo', default=True)

    def __str__(self):
        return f'ToDo {self.todo_text[1:20]}'

    class Meta:
        verbose_name = 'ToDo'
        verbose_name_plural = 'ToDo-s'

