from rest_framework import exceptions

from rest_framework.permissions import BasePermission

class Mypermission(BasePermission):
     message = 'Only VIP can allow to see'
     def has_permission(self,request,view):
         print(request.user.user_type)
         if request.user.user_type != 3:
             return False
         return True