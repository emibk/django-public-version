from django import forms

class ContactForm(forms.Form):
    username = forms.CharField(max_length=100, required=False)
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Adaugă mesajul...',
        })
        self.fields['text'].label = 'Adauga mesajul'
   
