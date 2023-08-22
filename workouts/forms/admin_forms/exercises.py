from django import forms
from workouts.models import Exercise

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = ['name', 'description', 'muscle_group']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Adauga descrierea..',
        })
        

class ExerciseDeleteForm(forms.Form):
    exercise_id = forms.IntegerField(widget=forms.HiddenInput)

    
