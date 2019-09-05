from django.db import models

# Create your models here.

class UserGroup(models.Model):
    uid = models.AutoField(primary_key=True)
    captions = models.CharField(max_length=50,unique=True)
    Nowtime = models.DateTimeField(auto_now_add=True,null=True)
    #uptime = models.DateTimeField(auto_now=True,null=True)


#obj = UserGroup.objects.filter(id=1).update(captions='B') 这种方式更新不了uptime，要使用下面的方法
# obj = UserGroup.objects.filter(id=1).first()
# obj.caption = 'B'
# obj.save()

#表名 a_userinfo
class UserInfo(models.Model):
    #id列 自增 主键
    #用户名列，字符串类型，指定长度
    username = models.CharField(max_length=32,verbose_name='用户名')
    password = models.CharField(max_length=64)
    email = models.CharField(max_length=15,null=True)
    #Django 创建时不是创建user_group 而是创建了user_group_id
    user_group = models.ForeignKey('UserGroup', to_field='uid',on_delete=models.CASCADE)  #user_group是类UserGroup的封装对象 user_group（uid，captions，Nowtime，uptime）

# user_list = UserInfo.objects.all()
# for row in user_list:
#     print(row.user_group_id)
#     print(row.user_group.captions)
#     print(row.user_group.Nowtime)
#     print(row.user_group.uid)
#     print(row.user_group.uptime)

class Host(models.Model):
    hostname = models.CharField(max_length=32)
    IP = models.CharField(max_length=32)

class Application(models.Model):
    name = models.CharField(max_length=10)
    r = models.ManyToManyField('Host')