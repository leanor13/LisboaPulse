from datetime import datetime
from urllib.parse import urlparse

from django.utils import timezone
from rest_framework import serializers

from .models import Event


def validate_date(value):
    if isinstance(value, datetime):
        if value < timezone.now():
            raise serializers.ValidationError("Event date must be in the future.")
        return value
    formats = [
        "%d-%m-%Y %H:%M",
        "%Y-%m-%d %H:%M",
        "%d/%m/%Y %H:%M",
        "%Y-%m-%dT%H:%M:%SZ",
    ]

    for fmt in formats:
        try:
            value = datetime.strptime(value, fmt)
            break
        except ValueError:
            continue
    else:
        raise serializers.ValidationError("Enter a valid date format.")

    if value < timezone.now():
        raise serializers.ValidationError("Event date must be in the future.")

    return value


def validate_url(value):
    parsed = urlparse(value)
    if not parsed.scheme:
        value_with_scheme = f"https://{value}"
        parsed = urlparse(value_with_scheme)
    else:
        value_with_scheme = value

    if not (parsed.scheme in ["http", "https"] and parsed.netloc):
        raise serializers.ValidationError("Enter a valid HTTPS URL.")

    return value_with_scheme


def validate_event_unique(data):
    if Event.objects.filter(
        title=data.get("title"),
        date=data.get("date"),
        source=data.get("source"),
    ).exists():
        raise serializers.ValidationError("This event already exists.")
    return data


class EventSerializer(serializers.ModelSerializer):

    source = serializers.CharField(validators=[validate_url])
    date = serializers.DateTimeField(validators=[validate_date])

    class Meta:
        model = Event
        fields = "__all__"

    def validate(self, data):
        return validate_event_unique(data)

    def create(self, validated_data):
        # TODO: check automatic added value. Make sure what to do with this pop, if it is necessary
        validated_data.pop("added_by", None)

        event = Event.objects.create(**validated_data)

        request = self.context.get("request")
        if request and request.user.is_authenticated:
            event.added_by = request.user.username
        else:
            event.added_by = "system"

        event.save()
        return event
