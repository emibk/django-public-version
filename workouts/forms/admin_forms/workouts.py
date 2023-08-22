from django import forms
from workouts.models import Workout, WorkoutDayExercise
from django.core.exceptions import ValidationError


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = ['name', 'disability', 'goal', 'equipment', 'level', 'length',
                  'description', 'image']
        widgets = {
            'image': forms.FileInput(attrs={'data-browse': 'Selecteaza Imaginea'})
        }
        

class WorkoutDeleteForm(forms.Form):
    workout_id = forms.IntegerField(widget=forms.HiddenInput)

class WorkoutDayExerciseForm(forms.ModelForm):
    class Meta:
        model = WorkoutDayExercise
        fields = ['exercise', 'specification', 'time', 'sets', 'repetitions']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['time'].widget.attrs['style'] = 'display:none;'
        self.fields['time'].required = False

    def clean(self):
        cleaned_data = super().clean()
        specification = cleaned_data.get('specification')
        time = cleaned_data.get('time')
        sets = cleaned_data.get('sets')
        repetitions = cleaned_data.get('repetitions')

        if specification == 'Timp' and (time is None or time <= 0):
            self.add_error('time', 'Please enter a valid time value.')

        if specification != 'Timp' and (sets is None or sets <= 0 or repetitions is None or repetitions <= 0):
            self.add_error(None, 'Please enter valid sets and repetitions values.')


class WorkoutDayExerciseDeleteForm(forms.Form):
    workoutexercise_id = forms.IntegerField(widget=forms.HiddenInput)
