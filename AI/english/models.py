from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

class Vocabulary(models.Model):
    word = models.TextField(max_length=100)
    mean = models.TextField(max_length=200)
    Toeic = models.BooleanField()
    Opic = models.BooleanField()
    korean_SAT = models.BooleanField()
