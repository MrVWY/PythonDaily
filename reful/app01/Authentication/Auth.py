from rest_framework import exceptions
from app01 import models
from rest_framework.authentication import  BaseAuthentication
from rest_framework.permissions import BasePermission

class MyAuthentication(object):
    def authenticate(self,request):
        token = request._request.GET.get('token')
        print(token)
        token_obj = models.UserToken.objects.filter(token=token).first()
        if not token_obj:
            raise  exceptions.AuthenticationFailed('用户认证失败')
        return (token_obj.user,token_obj)

    def authenticate_header(self,val):
        pass