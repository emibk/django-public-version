from django import forms
from workouts.models import FoodCalories

class CaloriesForm(forms.ModelForm):
    class Meta:
        model = FoodCalories
        fields = ['meal_type', 'food', 'calories']
