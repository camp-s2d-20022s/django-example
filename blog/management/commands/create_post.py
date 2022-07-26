from django.core.management.base import BaseCommand, CommandError
from blog import models

class Command(BaseCommand):
    help = 'Create Post'

    def add_arguments(self, parser):
        parser.add_argument('title', type=str)
        parser.add_argument('content', type=str)

    def handle(self, *args, **options):
        p = models.Post(title=options['title'],
                        content=options['content'])
        p.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully Created Post "{p.id}"'))