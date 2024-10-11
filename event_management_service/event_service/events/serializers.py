from django.utils import timezone
from rest_framework import serializers

from .models import Event


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

    def validate_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("Event date must be in the future.")
        return value
