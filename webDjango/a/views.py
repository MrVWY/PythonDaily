from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse
from django.shortcuts import render  #重定向不能用
from django.shortcuts import redirect   #重定向
from django.core.files.uploadedfile import InMemoryUploadedFile
import os
import json #test_ajax
from a import models

def login(request):
    error_msg = ''
    if request.method == 'GET' :
        return render(request, 'login.html')
    elif request.method == 'POST':
        # user = request.POST['user']
        # pwd = request.POST['pwd']
        # print(user,pwd)
        #使用上述的方法如果request.POST['1111'] 111不存在 程序就会报错
        user = request.POST.get('user', None)
        pwd = request.POST.get('pwd', None)
        print(user, pwd)
        obj = models.UserInfo.objects.filter(username=user,password=pwd).first()
        if obj:
            return redirect('/a/index/')
        else:
            #用户密码不匹配
            error_msg= '用户密码不匹配'
    return  render(request,'login.html',{'error_msg':error_msg})

# def login(request):
#     if request.method == 'GET':
#         return render(request,'login.html')
#     elif request.method == 'POST':
#         obj = request.FILES.get('uploadfile')
#         print(obj,type(obj),obj.name)
#         return render(request, 'login.html')
#     else:
#         return  redirect('/home')

user_list= [
    { 'username':'aaa','email':'123','age':'111'}
]
for index in range(20):
    temp = { 'username':'aaa'+str(index),'email':'123','age':'111'}
    user_list.append(temp)

def home(request): #request包括用户提交的所有信息
    #获取用户提交方法
    #print(request.method)
    if request.method == 'POST':
        u = request.POST.get('username',None)
        a = request.POST.get('email',None)
        s = request.POST.get('age',None)
        temp = { 'username':u,'email':a,'age':s}
        user_list.append(temp)
    return render(request,'home.html',{'user_list':user_list})

def zhuce(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        file = request.FILES.get('uploadfile')
        print(file, type(file), file.name)
        file_path = os.path.join('uploadfile', '2.jpg')
        f = open(file_path, mode='wb')
        for i in file.chunks():
            f.write(i)
        f.close()
        return render(request, 'register.html')
    else:
        return  redirect('/login')

#CBV模式
from django.views import View
class Home(View):

    def dispatch(self, request, *args, **kwargs):
        print('before')
        result = super(Home,self).dispatch(request, *args, **kwargs)
        print('after')
        return result

    def get(self,request):
        print(request.method)
        return render(request,'404.html')

    def post(self,request):
        print(request.method,'POST')
        return render(request, '404.html')

user_list_1 = {
    '1':{'name':'a','email':'123@163.com'},
    '2':{'name':'b','email':'123@163.com'},
    '3':{'name':'c','email':'123@163.com'},
}

def index(request):
    return render(request,'index.html',{'user_list_1':user_list_1})

def detail(request,aid):
    #return HttpResponse(aid)
    #aid = request.GET.get('aid')
    #print(uid)
    user_data = user_list_1[aid]
    return render(request,'detail.html',{'user_data':user_data})

#创建数据 添加进Navicat
def orm(request):
    #创建
    # models.UserInfo.objects.create(username='root',password='toor')
    # dic = {'username':'root2','password':'toor2'}
    # models.UserInfo.objects.create(**dic)
    #创建
    # obj = models.UserInfo(username='root1',password='toor1')
    # obj.save()
    #查
    #result = models.UserInfo.objects.all()
    #result.QuerySet => Django =>[]
    #[obj(id,username,password),obj(id,username,password),obj(id,username,password)]
    #result = models.UserInfo.objects.filter(username='root',password='toor')
    #删除
    #models.UserInfo.objects.filter(username='root', password='toor').delete()
    #更新
    #models.UserInfo.objects.all().update(password='1')
    # models.UserInfo.objects.filter(username='root').update(password='1')
    # for row in result:
    #     print(row.id,row.username,row.password)
    # models.UserGroup.objects.create(captions='BOSS')
    # models.UserGroup.objects.create(captions='CEO')
    # models.UserGroup.objects.create(captions='staff-mumber')
    # models.UserInfo.objects.create(username='root3',password='toor3',user_group_id='1')
    # models.UserInfo.objects.create(username='root4', password='toor4',user_group_id='2')
    # models.UserInfo.objects.create(username='root5', password='toor5',user_group_id='3')
    # models.UserInfo.objects.create(username='root6', password='toor6',user_group_id='1')
    # models.UserInfo.objects.create(username='root7', password='toor7',user_group_id='2')
    models.Host.objects.create(hostname='A1',IP='1.1.1.1')
    models.Host.objects.create(hostname='A2', IP='1.1.1.2')
    models.Host.objects.create(hostname='A3', IP='1.1.1.3')
    models.Host.objects.create(hostname='A4', IP='1.1.1.4')
    models.Host.objects.create(hostname='A5', IP='1.1.1.5')
    models.Host.objects.create(hostname='A6', IP='1.1.1.6')

    models.Application.objects.create(name='WEB')
    models.Application.objects.create(name='DB')
    models.Application.objects.create(name='python')



    return HttpResponse('ORM is OK')

def Backstage_login(request):
    return render(request,'Backstage_login.html')

def user_info(request):
    if request.method =='GET':
        user_list_2 = models.UserInfo.objects.all()
        user_list_3 = models.UserGroup.objects.all()
        #print(user_list_2.query)
        return render(request,'user_info.html',{'user_list_2':user_list_2,'user_list_3':user_list_3})
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_group_id = request.POST.get('group')
        models.UserInfo.objects.create(username=username,password=password,user_group_id=user_group_id)
        return redirect('/a/user_info')

def user_detail(request,nid):
    if request.method == 'GET':
        result = models.UserInfo.objects.filter(id = nid).first()
        user_list_3 = models.UserGroup.objects.all()
        #取单条数据 但是如果nid在数据库里面没有就报错 try...except
        #models.UserInfo.objects.get(id=nid)
        return  render(request,'user_detail.html',{'result':result,'user_list_3':user_list_3})
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_group_id = request.POST.get('group')
        models.UserInfo.objects.filter(id=nid).update(username=username,password=password,user_group_id=user_group_id)
        result = models.UserInfo.objects.filter(id=nid).first()
        return render(request,'user_detail.html',{'result':result})


def user_delete(request,nid):
    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/a/user_info')

def test_ajax(request):
    error_message = {'username_error':'','password_error':'','status':False}
    print(request.method,request.POST.get('username'),request.POST.get('password'))
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username and len(username)>5:
        if password and len(password)>5:
            error_message['status'] = True
            return  HttpResponse(json.dumps(error_message))
        else:
            error_message['password_error']='密码太短'
            return HttpResponse(json.dumps(error_message))
    else:
        error_message['username_error'] = '用户名太短'
        return HttpResponse(json.dumps(error_message))

def APP(request):
    if request.method == 'GET':
        user_list_10 = models.Application.objects.all()
        user_list_11 = models.Host.objects.all()
        return  render(request,'APP.html',{'user_list_10':user_list_10,'user_list_11':user_list_11})
    elif request.method == 'POST':
        groupname = request.POST.get('usergroup_name')
        hostlist = request.POST.getlist('group')

        new_group = models.Application.objects.create(name=groupname)
        new_group.r.add(*hostlist)

        return redirect('/a/APP')