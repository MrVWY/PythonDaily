"""分离 URL Configuration

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
from django.urls import path ,include
from django.urls  import  re_path
from app01 import views

from rest_framework import routers
router = routers.DefaultRouter()
router.register('page',views.V1)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('OrderView/',views.OrderView.as_view()),
    path('api/v100/Auth/',views.Auth.as_view()),
    path('UserInfo/',views.UserInfo.as_view()),
    re_path('app/(?P<version>[v1|v2]+)/Versionviews/',views.Versionviews.as_view()),
    re_path('app/(?P<version>[v1|v2]+)/RoleView/',views.RoleView.as_view()),
    re_path('app/(?P<version>[v1|v2]+)/UserView/',views.UserInfoView.as_view()),
    path('group/$',views.UserInfo_2_view.as_view()),
    re_path('group/(?P<pl>\d+)',views.GroupView.as_view(),name='gp'),
    #path('page/',views.PageView.as_view()),
    re_path('app/(?P<version>[v1|v2]+)/',include(router.urls)),
]
