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
from django.urls import path,include,re_path
from django.urls import re_path  #一个可以让你写正则表达式的路由

from b import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login),
    path('Custom_Paging/',views.Custom_Paging),
    path('index_b/',views.b_index),
    path('login_cookie_b/',views.b_login_cookie),
    path('login_Session_b/',views.login_Session_b),
    path('index_Session_b/',views.index_Session_b),
    re_path('loginout',views.loginout),
    path('test_middleware/',views.test_middleware)
]





