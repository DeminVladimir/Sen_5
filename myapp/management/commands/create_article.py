from django.core.management import BaseCommand
from random import choice
from apptwo.models import Article, Author

rand = [True, False]


class Command(BaseCommand):
    help = 'Create new user'

    def handle(self, *args, **options):
        article = Article(
            title="sefgwegfgs fasegf jgef jgf hg k,sgghehfh g",
            content='''jsfghjshg Sgkjhsefhf HghSg h sgkgj  JQH HFJK GBJGH  hgkhg AHfjdzhgkhzgnklsd ngSG hgnbjk 
                  ngiuerhrghawoi giohlk;jg hbn sLEGJ hzg kjsgiweugi ahhgzgh LKSJHGoi ygh  ng SEGio ayghioewgfj 
                  OPIGEJW49J GZHKBN KERHJ9EIYGH W87T HHS EH''',
            author=Author.objects.get(id=2),
            category='cats',
            views_count=1000000000,
            status=choice(rand)
        )

        article.save()