from django.db import models

# Create your models here.

class User(models.Model):
    user_name = models.CharField(max_length=264)
    phone_number = models.IntegerField(unique=True)
    date_of_birth = models.DateField()
    password = models.CharField(max_length=20)

