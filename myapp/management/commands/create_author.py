from django.core.management import BaseCommand
from apptwo.models import Author


class Command(BaseCommand):
    help = 'Create new user'

    def handle(self, *args, **options):
        author = Author(
            first_name='Alex',
            last_name='Orehov',
            email='areh@mail.ru',
            bio='fhwkfhg fh Ss hgSHG JHSLKF JLSGH SKN bkj zdbjn ',
            birthday='2000-10-11',
            fullname=''
        )

        author.fullname = author.full_name()
        author.save()
