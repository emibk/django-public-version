from django import forms
from workouts.models import Follow

class FollowForm(forms.ModelForm):
    class Meta:
        model = Follow
        fields = []

class UnfollowForm(forms.ModelForm):
    class Meta:
        model = Follow
        fields = []
