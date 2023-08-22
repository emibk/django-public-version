from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class Friendship(models.Model):
    id = models.AutoField(primary_key=True)
    user_1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_1")
    user_2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_2")

    def clean(self):
        if self.user1 == self.user2:
            raise ValidationError("User 1 and User 2 cannot be the same.")
        
    class Meta:
            ordering = ['user_1']

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return f"{self.user_1.username}'s friendship with {self.user_2.username} "
    @classmethod
    def send_friend_request(cls, sender_username, receiver_username):
        sender = User.objects.get(username=sender_username)
        receiver = User.objects.get(username=receiver_username)
        
        
        if cls.objects.filter(Q(user_1=sender, user_2=receiver) | Q(user_1=receiver, user_2=sender)).exists():
            return False  
        
        
        Friendship.objects.create(user_1=sender, user_2=receiver)
        return True
