from django.core.management import BaseCommand
from myapp.models import Author


class Command(BaseCommand):
    def handle(self, *args, **options):
        authors = Author.objects.all()
        self.stdout.write(f'{authors}')
