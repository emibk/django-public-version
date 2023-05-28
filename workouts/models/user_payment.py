from django.db import models
from django.contrib.auth.models import User

class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment #{self.id}"
