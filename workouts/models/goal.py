from django.db import models
from django.urls import reverse


class Goal(models.Model):
    goal_name = models.CharField(max_length=20, help_text='Dati numele scopului antrenamentului')

    class Meta:
        ordering = ['goal_name']

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.goal_name
