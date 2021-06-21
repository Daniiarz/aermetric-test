# Data validation and marshaling
from rest_framework import serializers

from . import models


class ChronicleSerializer(serializers.ModelSerializer):
    chronicle_events = serializers.ListField()

    class Meta:
        model = models.Chronicle
        fields = [
            'id',
            'min_timestamp',
            'max_timestamp',
            'status',
            'unique_id',
            'aircraft',
            'chronicle_events',
        ]
