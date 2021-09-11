  
from django.db import models

from django.contrib.auth.models import AbstractUser

from django.db import models
from django.db.models.enums import Choices

CHOICES = (
        ('MALE', 'male'),
        ('FEMALE', 'female'),
        
    )

class CustomUser(AbstractUser):
    email=models.CharField(max_length=200)
    gender=models.CharField(max_length=20 ,choices=CHOICES)

    def __str__(self):
        return self.username