from django.shortcuts import render

# Create your views here.


from django.shortcuts import HttpResponse
from django.shortcuts import redirect,render
from django.utils.safestring import mark_safe

def login(requrest):
    return HttpResponse('<h2>app:b  login</h2>')

class page_update:
    def __init__(self,Page,data_count,pre_page_count=10):
        self.Paging = Page
        self.data_count =data_count
        self.pre_page_count = pre_page_count

    @property
    def start(self):
        return (self.Paging-1)*self.pre_page_count

    @property
    def end(self):
        return self.Paging*self.pre_page_count

    @property
    def calculation(self):
        v, y = divmod(len(LIST), self.pre_page_count)
        if y:
            v += 1
        return v

    def page_pre(self):
        page_list = []
        if self.calculation < self.pre_page_count+1:
            start_index = 1
            end_index = self.calculation
        elif  self.Paging < 6:
            start_index = 1
            end_index = self.pre_page_count+1
        else:
            start_index =  self.Paging - 5
            end_index =  self.Paging + 6
            if end_index > self.calculation:
                end_index = self.calculation + 1

        if self.Paging == 1:
            tmp = '<a href="/b/Custom_Paging/?p=%s" class="page ">上一页</a>' % (self.Paging)
            # tmp = '<a href="javascript:void(0)" class="page ">上一页</a>'
        else:
            tmp = '<a href="/b/Custom_Paging/?p=%s" class="page ">上一页</a>' % (self.Paging - 1)
        page_list.append(tmp)

        for i in range(start_index, end_index):
            if i == self.Paging:
                tmp = '<a href="/b/Custom_Paging/?p=%s" class="page active">%s</a>' % (i, i)
            else:
                tmp = '<a href="/b/Custom_Paging/?p=%s" class="page">%s</a>' % (i, i)
            page_list.append(tmp)

        if self.Paging == self.calculation:
            tmp = '<a href="/b/Custom_Paging/?p=%s" class="page ">下一页</a>' % (self.calculation)
        else:
            tmp = '<a href="/b/Custom_Paging/?p=%s" class="page ">下一页</a>' % (self.Paging + 1)
        page_list.append(tmp)

        jump ='''
             <input type="text"/><a style="padding: 5px;background-color: black;color: white" onclick="jump(this,'/b/Custom_Paging/?p=')">跳转</a>
    <script>
            function jump(ths,base) {
                var value = ths.previousSibling.value;
                location.href = base + value
            }
    </script>
              
        '''
        page_list.append(jump)

        page_list = ''.join(page_list)
        return page_list

LIST = []
for i in range(1009):
    LIST.append(i)

def Custom_Paging(request):
    Paging = request.GET.get('p')
    Paging_number = int(Paging)

    Page_obj = page_update(Paging_number,len(LIST))
    Page_list = LIST[Page_obj.start:Page_obj.end]

    Paging_list_1 = '''
        <a href="/b/Custom_Paging/?p=4">4</a>
        <a href="/b/Custom_Paging/?p=5">5</a>
        <a href="/b/Custom_Paging/?p=6">6</a>
    '''
    Paging_list_2 = '''
         <a href="/b/Custom_Paging/?p=7">7</a>
        <a href="/b/Custom_Paging/?p=8">8</a>
        <a href="/b/Custom_Paging/?p=9">9</a>
    '''
    Paging_list_2 = mark_safe(Paging_list_2)

    page_list = Page_obj.page_pre()
    return render(request,'Custom_Paging.html',{'Paging_list':Page_list,'page_list':page_list})


user1 = {
   'a':{'pwd':'123'},
    'b': {'pwd': '123123'},
}

def b_login_cookie(request):
    error_msg = ''
    if request.method == 'GET':
        return render(request, 'login_cookie_b.html')
    elif request.method == 'POST':
        user = request.POST.get('username', None)
        pwd = request.POST.get('pwd', None)
        dio = user1.get(user)
        if not dio:
            error_msg = '用户名不存在'
            return render(request, 'login_cookie_b.html/', {'error_msg':error_msg})
        elif dio['pwd'] == pwd:
            res=redirect('/b/index_b')
            res.set_cookie('username123',user,max_age=10)
            return res
        else:
            error_msg= '用户密码不匹配'
            return render(request, 'login_cookie_b.html/', {'error_msg': error_msg})

def b_index(request):
    cookie = request.COOKIES.get('username123')
    if not cookie:
        return redirect('/b/login_cookie_b')
    return render(request, 'index_Cookie_b.html', {'cookie':cookie})


def login_Session_b(request):
    if request.method == 'GET':
        return render(request,'login_Seesion_b.html')
    elif request.method == 'POST':
        user = request.POST.get('username')
        pwd = request.POST.get('password')
        print(pwd)
        if user == '123' and pwd == '123':
            #Session中设置值
            request.session['username'] = user
            request.session['is_login'] = True
            if request.POST.get('free',None) == '1':
                #超时时间
                request.session.set_expiry(10)
            return redirect('/b/index_Session_b')
        else:
            return render(request,'login_Seesion_b.html')

def index_Session_b(request):
    #获取当前用户的随机字符串
    #根据随机字符串获取对应信息
    if request.session.get('is_login',None):
        return  render(request,'index_Session_b.html',{'username':request.session['username']})
    else:
        return HttpResponse('<h1>OUT<h1>')


def loginout(request):
    request.session.clear()
    return redirect('/b/login_Session_b')

def test_middleware(request):
    return HttpResponse('请看python-terminal')