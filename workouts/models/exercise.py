from django.core.validators import FileExtensionValidator
from django.db import models
from django.urls import reverse



class Exercise(models.Model):
    name = models.CharField(max_length=20, help_text='Dati numele exercitiului')
    description = models.TextField()

    muscle_group = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.name
