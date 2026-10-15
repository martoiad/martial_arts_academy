from django.db import models

from martial_arts.models import MartialArt


class Event(models.Model):
    EVENT_TYPE_CHOICES = (
        ('Seminar', 'Seminar'),
        ('Competition', 'Competition'),
        ('Gala', 'Gala'),
    )

    title = models.CharField(
        max_length=150,
    )

    event_type = models.CharField(
        max_length=20,
        choices=EVENT_TYPE_CHOICES,
    )

    description = models.TextField()

    date = models.DateField()

    location = models.CharField(
        max_length=150,
    )

    guest_name = models.CharField(
        max_length=100,
        blank=True,
    )

    martial_arts = models.ManyToManyField(
        MartialArt,
    )

    def __str__(self):
        return self.title