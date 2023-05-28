from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User


def image_path(instance, filename):
   
    return "users/" + instance.user.username + "/profile/" + "profile"+"." + filename.partition(".")[2]

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to=image_path, blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    current_weight = models.FloatField(null=True, blank=True)
    id = models.AutoField(primary_key=True)
    
    class Meta:
        ordering = ['user']

    def get_absolute_url(self):
        return reverse('model-detail-view', args=[str(self.id)])

    def __str__(self):
        return f'{self.user.username}\'s Profile'
    def save(self, *args, **kwargs):
        # delete old file if this is an update
        try:
            this = UserInfo.objects.get(id=self.id)
            if this.profile_image != self.profile_image:
                this.profile_image.delete(save=False)
        except UserInfo.DoesNotExist:
            pass

        # save new file
        super(UserInfo, self).save(*args, **kwargs)
