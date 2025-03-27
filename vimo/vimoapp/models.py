from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import get_user_model
class User(AbstractUser):

#Create your models here.
 class CustomUser(AbstractUser):
    username = models.CharField(max_length = 20,blank = True,null = True)
    password = models.CharField(max_length = 20,blank = True,null = True)
    email = models.EmailField(max_length = 20,blank = True,null = True)

    def __str__(self):
        return self.username

    