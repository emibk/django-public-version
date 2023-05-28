import re

from django.utils.translation import gettext_lazy as _

from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from .disability import Disability
from .goal import Goal


def validate_length(value):
    if value <= 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )


def image_path(instance, filename):
    #return "workouts/" + instance.name + "." + filename.partition(".")[1]
    return "workouts/" + instance.name + "." + filename.partition(".")[2]

class Workout(models.Model):
    name = models.CharField(max_length=20, help_text='Denumiti antrenamentul')
    disability = models.ForeignKey(Disability, on_delete=models.CASCADE, null=True, blank=True)
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE, null=True, blank=True)
    equipment_choices = (
        ("Nu, antrenament acasa", "Nu, antrenament acasa"),
        ("Da, antrenament la sala", "Da, antrenament la sala"),
    )
    equipment = models.CharField(max_length=25, choices=equipment_choices, default="Nu, antrenament acasa")
    level_choices = (
        ("Incepator", "Incepator"),
        ("Mediu", "Mediu"),
        ("Avansat", "Avansat"),
    )
    level = models.CharField(max_length=20, choices=level_choices, default="Incepator")
    length = models.IntegerField(validators=[validate_length], help_text="Numarul de zile")
    description = models.TextField()
    image = models.ImageField(upload_to=image_path, blank=True, null=True)

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        # delete old file if this is an update
        try:
            this = Workout.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete(save=False)
        except Workout.DoesNotExist:
            pass

        # save new file
        super(Workout, self).save(*args, **kwargs)
