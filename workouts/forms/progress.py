from django import forms
from workouts.models import Progress

class ProgressForm(forms.ModelForm):
    class Meta:
        model = Progress
        fields = []