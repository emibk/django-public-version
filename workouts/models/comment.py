from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from .post import Post

class Comment(models.Model):
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    parent_comment = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='replies')
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment by {self.user.username} on post {self.post.id}'

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.post.id)])