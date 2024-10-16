from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    date = models.DateTimeField(db_index=True)
    venue = models.CharField(max_length=255, db_index=True)
    address = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    event_type = models.CharField(max_length=255, db_index=True)
    source = models.CharField(max_length=255)
    comments = models.TextField(blank=True, null=True)
    added_by = models.CharField(max_length=50, blank=True, null=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["title", "date", "source"], name="unique_event_constraint"
            )
        ]

    def __str__(self):
        return self.title

    def clean(self):
        if self.date < timezone.now():
            raise ValidationError("The event date must be in the future.")
