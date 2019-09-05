from django.shortcuts import render
import re
# Create your views here.
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django import forms
from a import models
from django.forms import fields
from django.forms import widgets
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

class FM(forms.Form):

    user = fields.CharField(
        required=True,  # 必填字段
        widget= widgets.TextInput(attrs={'class':'c1','placeholder':u'用户名'}),
        error_messages={'required':'用户名不能为空'},
        #initial = 'root',
        label='用户名:',
    )
    pwd = fields.CharField(
        max_length=12,
        min_length=6,
        error_messages={'required':'密码不能为空','max_length':'密码长度不能大于12位','min_length':'密码长度不能小于6位'},
        widget=widgets.PasswordInput(attrs={'class':'c3','placeholder':u'密码'}),
        label='密码:',
    )
    email = fields.EmailField(
        widget=widgets.TextInput(attrs={'class': 'c4', 'placeholder': u'email'}),
        error_messages={'required':'email不能为空','invalid':'email格式错误'},
        label='email:',
    )
    phonenumber = fields.CharField(
        max_length=12,
        widget=widgets.TextInput(attrs={'class': 'c5', 'placeholder': u'手机号'}),
        validators = [RegexValidator(r'^[0-9]+$','请输入数字'),RegexValidator(r'^139[0-9]+$','数字必须以139开头')],
        label='phonenumber:',
     )

def index(request):
    #return render(request,'first_login.html')
    error_message = ''
    if request.method == 'GET':
        return  render(request,'first_login.html')
    elif request.method == 'POST':
        username_or_phone = request.POST.get('username_or_phone')
        password = request.POST.get('password')
        remember = request.POST.get('remember')
        if username_or_phone == 'root'  and password == 'toor':
            return redirect('/c/cache')
        else:
            error_message = '滚蛋'
    return render(request,'first_login.html',{'error_message':error_message})

def register(request):
    if request.method == 'GET':
        obj = FM()
        return render(request,'register.html',{'obj':obj})
    elif request.method == 'POST':
        obj = FM(request.POST)
        b = obj.is_valid()
        if b:
            print(obj.cleaned_data)

        else:
            print(obj.errors.as_json())
            return render(request,'register.html',{'obj':obj})
    return render(request,'register.html')
