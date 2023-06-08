from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone


class FoodCalories(models.Model):
    MEAL_CHOICES = [
        ('Mic Dejun', 'Mic Dejun'),
        ('Gustare', 'Gustare'),
        ('Pranz', 'Pranz'),
        ('Cina', 'Cina'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    meal_type = models.CharField(max_length=20, choices=MEAL_CHOICES)
    food = models.CharField(max_length=100)
    calories = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.user} - {self.date}, calories {self.calories}'

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

