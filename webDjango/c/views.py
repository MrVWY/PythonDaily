from django.shortcuts import render

# Create your views here.

from django.shortcuts import redirect,render,HttpResponse
import time
import re
import json
import os
from django import forms
from a import models
from django.forms import fields
from django.forms import widgets
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

from django.views.decorators.cache import  cache_page
@cache_page(10)
def cache(request):
    ctime = time.time()
    return render(request,'cache.html',{'ctime':ctime})


class FM(forms.Form):

    def mobile_validate(value):
        mobile_re = re.compile(r'^666[0-9]+$')
        if  mobile_re.match(value):
            raise ValidationError('手机号码格式错误')

    #调用
    def clean_username(self):
        value = self.cleaned_data['phonenumber_2']
        if "666" in value:
            try:
                raise ValidationError('666已经被玩烂了...', 'invalid')
            except:
                print('666已经被玩烂了')
                username = '666已经被玩烂了'
                return username
        return value

    user = fields.CharField(
        required=True,  # 必填字段
        widget= widgets.TextInput(attrs={'class':'c1','placeholder':u'用户名'}),
        error_messages={'required':'用户名不能为空'},
        initial = 'root',
        label='用户名',
    )
    pwd = fields.CharField(
        max_length=12,
        min_length=6,
        error_messages={'required':'密码不能为空','max_length':'密码长度不能大于12位','min_length':'密码长度不能小于6位'},
        widget=widgets.PasswordInput(attrs={'class':'c3','placeholder':u'密码'})
    )
    email = fields.EmailField(
        widget=widgets.TextInput(attrs={'class': 'c4', 'placeholder': u'email'}),
        error_messages={'required':'email不能为空','invalid':'email格式错误'}
    )
    phonenumber = fields.CharField(
        max_length=12,
        widget=widgets.TextInput(attrs={'class': 'c5', 'placeholder': u'手机号'}),
        validators = [RegexValidator(r'^[0-9]+$','请输入数字'),RegexValidator(r'^139[0-9]+$','数字必须以139开头')]
     )
    phonenumber_1 = fields.CharField(
        max_length=12,
        widget=widgets.TextInput(attrs={'class': 'c5', 'placeholder': u'手机号1'}),
        validators=[mobile_validate, ],
    )
    phonenumber_2 = fields.CharField(
        max_length=12,
        widget=widgets.TextInput(attrs={'class': 'c6', 'placeholder': u'手机号2'}),
        validators=[RegexValidator(r'^[0-9]+$', 'Enter a valid extension.', 'invalid')],
    )


def Form_base_Django(request):
    if request.method == 'GET':
        obj = FM()
        return render(request,'Form_base_Django.html',{'obj':obj})
    elif request.method == 'POST':
        obj = FM(request.POST)
        b = obj.is_valid()
        user_errors = obj.clean_username()
        if b:
            print(obj.cleaned_data)
            #models.UserInfo.objects.create(**obj.cleaned_data)
        else:
            print(obj.errors.as_json())
            print(user_errors)
            #print(obj.errors["user"])
        return render(request,'Form_base_Django.html',{'obj':obj,'user_errors':user_errors})
    return render(request,'Form_base_Django.html')

def ajax(request):
    return render(request,'c_ajax_post.html')

def ajax_post(request):
    print(request.POST)
    rep = {'code':True,'data':'sabc'}
    return HttpResponse(json.dumps(rep))


def upload(request):
    return render(request,'c_upload.html')

def upload_file(request):
    #username = request.POST.get('username')
    file_obj = request.FILES.get('file')
    print(file_obj)
    #print(username)
    img_path = os.path.join('static/img/',file_obj.name)
    print(img_path)
    with open(img_path,'wb') as f:
        for item in file_obj.chunks():
            f.write(item)
    f.close()
    rep = {'data':img_path}
    return HttpResponse(json.dumps(rep))
