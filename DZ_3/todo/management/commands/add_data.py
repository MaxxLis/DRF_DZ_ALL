from django.core.management.base import BaseCommand
from todo.models import Project, Todo
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        Project.objects.create(name_project='Восстание', users_project=str(User.objects.all()[1]))
        Project.objects.create(name_project='Упадок', users_project=str(User.objects.all()[0]))
        Project.objects.create(name_project='Прорыв', users_project=str(User.objects.all()[2]))
        print('Проекты - созданы')
        # Todo.objects.create(todo_project='')
        #
        # todo_project = models.ForeignKey(Project, on_delete=models.CASCADE)
        # todo_user = models.ForeignKey(User, on_delete=models.CASCADE)
        # todo_text = models.CharField('Текст заметки', max_length=200)
        # todo_date_create = models.DateTimeField('Время создания заметки')
        # todo_date_update = models.DateTimeField('Время изменения заметки')
        # todo_open_close = models.BooleanField('Открыта или зактыта ToDo', default=True)