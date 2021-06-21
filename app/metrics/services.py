# Business logic goes here

from .models import Chronicle


def get_chronicle(unique_id):
    """
    Get chronicle with events list of n entities
    :param unique_id: Chronicle id
    :return: Chronicle with events list
    """
    default_range = 20
    chronicle = _query_chronicle(unique_id)
    if len(chronicle.chronicle_events) < default_range:
        chronicle.chronicle_events.extend([0 for i in range(default_range - len(chronicle.chronicle_events))])

    return chronicle


def _query_chronicle(unique_id):
    chronicle = Chronicle.objects.raw("select *, array(select case when count(e.unique_id) > 0 then 1 else 0 end "
                                      "from generate_series("
                                      "date(chronicle.min_timestamp), "
                                      "date(chronicle.max_timestamp), '1 DAY') as dates "
                                      "left join event as e on dates = e.datetime group by dates order by dates desc) "
                                      "as chronicle_events "
                                      "from chronicle where unique_id = %s", params=(unique_id,))

    return next(chronicle.iterator())
