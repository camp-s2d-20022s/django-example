from django.core.management.base import BaseCommand, CommandError
from polls import models

class Command(BaseCommand):
    help = 'Create Question'

    def add_arguments(self, parser):
        parser.add_argument('title', type=str)
        parser.add_argument('content', type=str)

    def handle(self, *args, **options):
        q = models.Question(title=options['title'],
                            content=options['content'])
        q.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully closed Question "{q.id}"'))