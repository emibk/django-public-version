from django import forms
from workouts.models import Disability

class DisabilityForm(forms.ModelForm):
    class Meta:
        model = Disability
        fields = ['name']
        

class DisabilityDeleteForm(forms.Form):
    disability_id = forms.IntegerField(widget=forms.HiddenInput)

    
