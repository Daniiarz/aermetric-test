from django.core.management import BaseCommand
from django.utils import timezone

from metrics.models import Chronicle, Event


class Command(BaseCommand):

    def handle(self, *args, **options):
        Chronicle.objects.create(min_timestamp=timezone.datetime(2021, 5, 24),
                                 max_timestamp=timezone.datetime(2021, 5, 25),
                                 unique_id="440AS-924942",
                                 aircraft='440AS')
        Event.objects.create(datetime=timezone.datetime(2021, 5, 25),
                             unique_id="440AS-924942",
                             aircraft='440AS')