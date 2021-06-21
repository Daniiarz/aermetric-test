import pytest

from metrics import services


@pytest.mark.django_db
def test_query_chronicle(new_chronicle):
    chronicle = services._query_chronicle(new_chronicle.unique_id)

    assert len(chronicle.chronicle_events) == 0


@pytest.mark.django_db
def test_get_chronicle(new_chronicle, new_event):
    chronicle = services.get_chronicle(new_chronicle.unique_id)
    assert len(chronicle.chronicle_events) == 20
    assert chronicle.chronicle_events[0] == 1
