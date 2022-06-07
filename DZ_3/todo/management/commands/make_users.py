from django.core.management.base import BaseCommand
from django.contrib.auth.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        User.objects.create_superuser('django', password='geekbrains')
        User.objects.create_user('Max_test', password='123456789qq')
        User.objects.create_user('Nico_test', password='123456789ww')
        print(f'Пользователи django, Max_test, Nico_test - созданы')