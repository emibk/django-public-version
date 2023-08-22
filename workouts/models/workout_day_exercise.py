from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from .workout_day import WorkoutDay
from django.utils.translation import gettext_lazy as _
from .exercise import Exercise


def validate(value):
    if value < 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )


class WorkoutDayExercise(models.Model):
    workout_day = models.ForeignKey(WorkoutDay, on_delete=models.CASCADE)
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    specification_choices = (
        ("Timp", "Timp"),
        ("Seturi si Repetitii", "Seturi si Repetitii"),
    )
    specification = models.CharField(max_length=20, choices=specification_choices,
                                     default="Seturi si Repetitii")
    time = models.IntegerField(validators=[validate], default=0)
    sets = models.IntegerField(validators=[validate], default=0)
    repetitions = models.IntegerField(validators=[validate], default=0)

    class Meta:
        ordering = ['workout_day']
        
    @property
    def workout_name(self):
        return self.workout_day.workout.name

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.exercise.name + " " + str(self.workout_day.day) + " " + self.workout_day.workout.name
