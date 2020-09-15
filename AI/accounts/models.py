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

class DateCount(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    image_speak_count = models.IntegerField(default='0')
    text_speak_count = models.IntegerField(default='0')
    listening_count = models.IntegerField(default='0')