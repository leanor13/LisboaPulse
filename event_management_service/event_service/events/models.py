from django.core.exceptions import ValidationError
from django.db import models
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(max_length=255)
    date = models.DateTimeField()
    venue = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    event_type = models.CharField(max_length=255)
    source = models.URLField()
    comments = models.TextField(blank=True, null=True)
    # TODO: automatically define who added info
    added_by = models.CharField(
        max_length=50, choices=[("scraper", "Lisboa Pulse"), ("user", "User")]
    )
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
