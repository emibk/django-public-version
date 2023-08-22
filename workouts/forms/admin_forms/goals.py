from django import forms
from workouts.models import Goal

class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['goal_name']
        

class GoalDeleteForm(forms.Form):
    goal_id = forms.IntegerField(widget=forms.HiddenInput)

    
