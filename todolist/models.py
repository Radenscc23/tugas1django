from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Task (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default = timezone.now)
    title = models.TextField(max_length = 250)
    description = models.TextField(null=True)
    is_finished = models.BooleanField(default=False)