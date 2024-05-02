from django.core.management.base import BaseCommand, CommandError
from maintable.models import Post


class Command(BaseCommand):
    help = 'Удаление всех новостей'
    requires_migrations_checks = True

    def handle(self, *args, **options):
        self.stdout.readable()
        self.stdout.write('Вы действительно хотите удалить все новости? да/нет')
        answer = input()

        if answer == 'да':
            Post.objects.all().delete()
            self.stdout.write(self.style.SUCCESS('Новости успешно удалены!'))
            return

        self.stdout.write(self.style.ERROR('Удаление невозможно!'))
