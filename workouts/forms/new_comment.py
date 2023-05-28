from django import forms
from workouts.models import Comment

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('text', 'parent_comment',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['text'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Adaugă un comentariu...',
        })
        self.fields['text'].label = 'Adauga un nou comentariu'
