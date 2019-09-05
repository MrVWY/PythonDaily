from rest_framework.views import APIView
from django.shortcuts import HttpResponse
from app01 import models
import json
import hashlib
import time
from rest_framework.versioning import URLPathVersioning
from rest_framework import serializers

from django.views import  View
from rest_framework import exceptions
from rest_framework.throttling import BaseThrottle
from rest_framework.request import Request
from rest_framework.versioning import  QueryParameterVersioning
from django.core.handlers.wsgi import  WSGIRequest
from rest_framework.parsers import JSONParser

def md5(user):
    ctime = str(time.time())
    m = hashlib.md5(bytes(user,encoding='utf-8'))
    m.update(bytes(ctime,encoding='utf-8'))
    return m.hexdigest() #返回一个十六进制打数据字符串值

class Auth(APIView):
    ''' 用户登陆认证 '''
    authentication_classes = []
    permission_classes = []
    def post(self,request,*args,**kwargs):
        ret = {'code':200,'message':None}
        try:
            username  = request._request.POST.get('username')
            print(username)
            password = request._request.POST.get('password')
            print(password)
            obj = models.UserInfo.objects.filter(username=username,password=password).first()
            if not obj:
                ret['code'] = 404
                ret['message']='用户名或密码错误'
            token = md5(username)
            print(token)
            models.UserToken.objects.update_or_create(user=obj,defaults={'token':token})
            ret['token'] = token
        except Exception as e:
            ret['code'] = 404
            ret['message'] = '请求错误'
        return HttpResponse(json.dumps(ret))

    def get(self,request,*args,**kwargs):
        return HttpResponse('OK')


class OrderView(APIView):
    #authentication_classes = []
    #permission_classes = []
    def post(self,request,*args,**kwargs):
       #self.dispatch()
       print(request)
       print(request.user,request.auth)
       print(request.user)

       order ={
           'code':1000,
           'msg': None,
           'data': '你好'
       }
       return HttpResponse(json.dumps(order))

class UserInfo(APIView):
    def get(self,request,*args,**kwargs):
        print(request.user)
        return HttpResponse('用户信息')

#版本
# class ParamVersion(object):
#     def determine_version(self,request,*args,**kwargs):
#         version = request.query_params.get('version')
#         return version

class Versionviews(APIView):
    versioning_class = URLPathVersioning
    authentication_classes = []
    permission_classes = []
    def get(self,request,*args,**kwargs):
        #version = request._request.GET.get('verison')
        #print(version)
        # version = request.query_params.get('version')
        # print(version)
        print(request.version)
        return HttpResponse('OK')


#序列化
class RolesSerializer(serializers.Serializer):
    ID = serializers.IntegerField(source='id')
    position = serializers.CharField()

class RoleView(APIView):
    versioning_class = URLPathVersioning
    authentication_classes = []
    permission_classes = []
    def get(self,request,*args,**kwargs):
        roles = models.Role.objects.all()
        ser = RolesSerializer(instance=roles,many=True)
        ret = json.dumps(ser.data,ensure_ascii=False)
        return  HttpResponse(ret)

class UserSerializer(serializers.Serializer):
    UT = serializers.IntegerField(source='user_type')
    UTN = serializers.CharField(source='get_user_type_display')
    gp = serializers.CharField(source = 'group.type')
    username  = serializers.CharField()
    password = serializers.IntegerField()
    #r_list = serializers.CharField(source='roles.all')
    rlist = serializers.SerializerMethodField() # 自定义显示

    def get_rlist(self,row):
        role_list = row.roles.all()
        ret = []
        for item in role_list:
            ret.append( {'id':item.id,'title':item.position})
        return ret

class UserInfoView(APIView):
    versioning_class = URLPathVersioning
    authentication_classes = []
    permission_classes = []
    def get(self,request,*args,**kwargs):
        roles = models.UserInfo.objects.all()
        ser = UserSerializer(instance=roles,many=True)
        ret = json.dumps(ser.data,ensure_ascii=False)
        return  HttpResponse(ret)


#hypermedialink
class UserInfo_2_serializers(serializers.ModelSerializer):
    group = serializers.HyperlinkedIdentityField(view_name='gp',lookup_field='group_id',lookup_url_kwarg='pl')# lookup_field:根据表指定字段

    # 指定一个Model，自动检测序列化的字段
    class Meta:
        model = models.UserInfo
        fields = ['id','username','password','group']
        #extra_kwargs = {'group':{'source':'group.type'},}
        depth = 0 #0-10之间


class UserInfo_Serializers(serializers.Serializer):
    name = serializers.CharField(error_messages={'required':'不能为空'},validators=[])

class UserInfo_2_view(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self, request, *args, **kwargs):
        roles = models.UserInfo.objects.all()
        ser = UserInfo_2_serializers(instance=roles, many=True,context={'request':request})
        ret = json.dumps(ser.data, ensure_ascii=False)
        return HttpResponse(ret)

    def post(self, request, *args, **kwargs):
        ser = UserInfo_Serializers(data=request.data)
        if ser.is_valid():
            print(ser.validated_data['name'])
        else:
            print(ser.errors)

        return HttpResponse('LLLLL')

class Groupserializers(serializers.ModelSerializer):
    class Meta:
        model = models.Usergroup
        fields = "__all__"

class GroupView(APIView):
    authentication_classes = []
    permission_classes = []
    def get(self,request,*args,**kwargs):
        pk = kwargs.get('pl')
        print(pk)
        obj = models.Usergroup.objects.filter(pk=pk).first()
        print(obj)
        ser = Groupserializers(instance=obj,many=False)
        ret = json.dumps(ser.data,ensure_ascii=False)
        return HttpResponse(ret)

#分页
from rest_framework.response import Response
from rest_framework.pagination import  PageNumberPagination #分页1
from rest_framework.pagination import LimitOffsetPagination #分页2 在n个位置，向后查看n条数据
from rest_framework.pagination import CursorPagination  #加密分页
class Pageserializers(serializers.ModelSerializer):
    class Meta:
        model = models.Role
        fields = "__all__"

class CustomPage(PageNumberPagination):
    page_size = 2
    page_size_query_param = 'page_size'
    max_page_size = 3
    page_query_param = 'page'

class PageView(APIView):
     authentication_classes = []
     permission_classes = []
     def get(self,request,*args,**kwargs):
         #获取所有数据
         roles = models.Role.objects.all()
         #创建分页对象
         sg = CustomPage()
         #在数据库获取分页的数据
         pager_roles = sg.paginate_queryset(queryset=roles,request=request,view=self)
         print(pager_roles)
         #对分页数据序列化
         ser = Pageserializers(instance=pager_roles, many=True)

         #return sg.get_paginated_response(data=ser.data)  可以传下页URL
         return Response(ser.data)

from rest_framework.generics import GenericAPIView
from rest_framework.viewsets import GenericViewSet
from rest_framework.viewsets import ModelViewSet
class V1(ModelViewSet):
    queryset = models.Role.objects.all()
    serializer_class = Pageserializers
    pagination_class = PageNumberPagination
    # def get(self,request,*args,**kwargs):
    #     #获取数据
    #     roles = self.get_queryset() # queryset -> models.Role.objects.all()
    #     pager_roles = self.paginate_queryset(roles)
    #     ser = self.get_serializer(instance=pager_roles,many=True)
    #     return Response(ser.data)

from rest_framework.renderers import JSONRenderer , BrowsableAPIRenderer ,AdminRenderer,HTMLFormRenderer