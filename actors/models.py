from django.db import models
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser


class Customer(models.Model):
    name = models.CharField(max_length=255,null=True)
    roll_no = models.CharField(max_length=255, primary_key=True)
    # balance = models.CharField(max_length=50,null=True)
    # roll_no = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class User(AbstractUser):
    username = models.CharField(max_length=50, unique=True, null=False,blank=True)
    name = models.CharField(max_length=50,null=True)
    contact = models.CharField(max_length=50,null=True)
    image = models.ImageField(upload_to='pics/', blank=True)





