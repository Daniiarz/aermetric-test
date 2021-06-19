from django.db import models


# Create your models here.
class Chronicle(models.Model):
    """
    Storing chronicles with specified length to keep events that happen within that date
    """
    OPEN = "open"
    CLOSED = 'closed'
    _status = (
        ("Open", OPEN),
        ("Closed", CLOSED),
    )
    min_timestamp = models.DateTimeField()
    max_timestamp = models.DateTimeField()
    status = models.CharField(max_length=15, choices=_status, default=OPEN)
    unique_id = models.CharField(max_length=50)
    aircraft = models.CharField(max_length=50)

    class Meta:
        db_table = "chronicle"

    def __str__(self):
        return f"{self.aircraft} {self.min_timestamp}-{self.max_timestamp}"

