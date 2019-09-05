from django.db import models

# Create your models here.
class UserGroup(models.Model):
    uid = models.AutoField(primary_key=True)
    caption  = models.CharField(max_length=50,unique=True)



class UserInfo(models.Model):
    username = models.CharField(max_length=12)
    password = models.CharField(max_length=12)
    email = models.CharField(max_length=12)
    phonenumber = models.IntegerField(max_length=12)

