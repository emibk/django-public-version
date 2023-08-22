from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from .workout import Workout


def validate_day(value):
    if value <= 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )


class WorkoutDay(models.Model):
    day = models.IntegerField(validators=[validate_day], help_text="Numarul zilei")
    workout = models.ForeignKey(Workout, on_delete=models.CASCADE)

    class Meta:
        ordering = ['day']

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return str(self.day) + " " + self.workout.name;
