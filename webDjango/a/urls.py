"""webDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.urls import re_path  #一个可以让你写正则表达式的路由

from a import views

urlpatterns = [
    path('admin/', admin.site.urls),#Django后台管理
    path('home/', views.home),
    path('login/',views.login),
    path('zhuce/',views.zhuce),
    path('404/',views.Home.as_view()),
    re_path('detail-(\d+).html/',views.detail),
    #re_path('detail-(?P<uid>\d+)-(?P<nid>\d+).html/',views.detail), #第一个获取的值给nid 第二个获取的值给uid
    path('orm/',views.orm),
    path('user_info',views.user_info),
    path('Backstage_login/',views.Backstage_login),
    re_path('userdetail-(?P<nid>\d+)',views.user_detail),
    re_path('userdelete-(?P<nid>\d+)',views.user_delete),
    path('test_ajax',views.test_ajax),  #Ajax
    path('index/',views.index,name='index123'), #name 相当于一个标记 （请看index.html）   name的设置只能获取到index/555 中的index  后面获取不到 需要在index.html中{% url 'index123'555 %}
    path('APP/',views.APP) #多对多关系库
]
