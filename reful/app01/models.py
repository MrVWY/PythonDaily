from django.db import models

class UserInfo(models.Model):
    user_type = (
        (1,'普通用户'),
        (2,'VIP'),
        (3,'SVIP'),
    )
    username = models.CharField(max_length=12,unique=True)
    user_type = models.IntegerField(choices=user_type)
    password = models.CharField(max_length=12)
    roles = models.ManyToManyField('Role')
    group = models.ForeignKey('Usergroup',on_delete=models.CASCADE)


class UserToken(models.Model):
    user = models.OneToOneField(to=UserInfo,on_delete=models.CASCADE)
    token = models.CharField(max_length=64)

class Role(models.Model):
    position = models.CharField(max_length=32)

class Usergroup(models.Model):
    type = models.CharField(max_length=12)