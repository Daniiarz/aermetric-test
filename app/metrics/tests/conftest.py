import pytest
from django.utils import timezone

from metrics import models


@pytest.fixture
def new_chronicle():
    chronicle = models.Chronicle.objects.create(min_timestamp=timezone.now(),
                                                max_timestamp=timezone.now() + timezone.timedelta(days=1),
                                                unique_id="ghoul-sss",
                                                aircraft='Boeing-747')

    return chronicle


@pytest.fixture
def new_event():
    event = models.Event.objects.create(datetime=timezone.now(),
                                        unique_id="ghoul-sss",
                                        aircraft='Boeing-747')

    return event
