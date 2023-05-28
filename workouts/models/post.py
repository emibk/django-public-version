from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
def image_path(instance, filename):  
    return "users/" + instance.user.username + "/posts/" + str(instance.id) +"." + filename.partition(".")[2]

class Post(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    title = models.CharField(max_length=20, help_text='Titlul postarii')
    picture = models.ImageField(upload_to=image_path, blank=True, null=True)
    text = models.TextField(blank=True,null=True)
    time = models.DateTimeField(auto_now_add=True)
    post_choices = (
        ("Schimbare in greutate", "Schimbare in greutate"),
        ("Alt tip de postare", "Alt tip de postare"),
    )
    post_type = models.CharField(max_length=30, choices=post_choices, default="Alt tip de postare")

    class Meta:
            ordering = ['user']

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return f"{self.user.username}'s Post: {self.title}"