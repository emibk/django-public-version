from django import forms
from workouts.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'picture', 'text', 'post_type']
