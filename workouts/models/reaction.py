from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .post import Post

class Reaction(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="reactions")
    time = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="reactions")

    class Meta:
            ordering = ['post']

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return f"{self.user.username}'s reaction on {self.post.title} "
