from django import forms

class EmailUpdateForm(forms.Form):
    new_email = forms.EmailField()
