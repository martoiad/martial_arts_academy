from django.db import models

from martial_arts.models import MartialArt


class CurriculumItem(models.Model):
    LEVEL_CHOICES = (
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    )

    name = models.CharField(
        max_length=100,
    )

    description = models.TextField()

    level = models.CharField(
        max_length=20,
        choices=LEVEL_CHOICES,
    )

    martial_art = models.ForeignKey(
        MartialArt,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name