class Request(object):
    def __init__(self,obj):
        self.obj = obj

    def user(self):
        return self.obj.authicate()

class Auth(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def authticate(self):
        return True

class APIView(object):
    def dispath(self):
        self.f2()

    def f2(self):
        a = Auth('I Love U ' , '18')
        req = Request(a)
        print(req)

obj = APIView()
obj.dispath()