
from django.forms import ModelForm
from workouts.models import UserInfo
from django import forms
from django.forms.widgets import DateInput
from datetime import date


class UserInfoForm(ModelForm):
    class Meta:
        model = UserInfo
        fields = ['profile_image','date_of_birth','current_weight'] 
        widgets = {
            'date_of_birth': DateInput(attrs={'id': 'date_of_birth', 'class': 'form-control'}),
            'profile_image': forms.FileInput(attrs={'data-browse': 'Selecteaza Imaginea'})
        }
    
    def clean_date_of_birth(self):
        date_of_birth = self.cleaned_data['date_of_birth']
        if date_of_birth >= date(2006, 1, 1) or date_of_birth <= date(1920, 1, 1):
            raise forms.ValidationError('Please enter a valid date of birth')
        return date_of_birth
