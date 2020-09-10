from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    total_point = models.IntegerField(default=0)

class Point(models.Model):
    use_type = models.BooleanField()
    value = models.IntegerField()
    content = models.TextField(max_length=50)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)