from django.db import models
from django.urls import reverse


class Disability(models.Model):
    name = models.CharField(max_length=200, help_text='Dati numele dizabilitatii')

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.name
