from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .workout_day import WorkoutDay

class Progress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    workout_day = models.ForeignKey(WorkoutDay, on_delete=models.CASCADE)
    class Meta:
            ordering = ['user']

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])
    
    def get_workout_name(self):
        return self.workout_day.workout.name

    def __str__(self):
        return f"{self.user.username}'s progress on {self.workout_day.day} "
