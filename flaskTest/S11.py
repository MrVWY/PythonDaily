class foo(object):

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        return '666'

    def __str__(self):
        return '11111'

class FOO(object):

    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        return super(FOO,cls).__new__(cls, *args, **kwargs)


class Foo(object):

    def __str__(self):
        return '22222'

obj = foo()
OBJ = FOO()
Obj = Foo()

print(obj)
print(OBJ)
print(Obj)


class A(object):
    B = 123
    def __init__(self,na):
        self.name = na

print(A.__dict__)#A是个类
print(dir(A))#把里面封装所有东西的key全部拿到

obj = A('majiko')
print(obj.__dict__)#obj是个对象


class F1(object):
    pass

class F2(object):
    pass

class F3(F2):
    pass

class F4(F1):
    pass

class F5(F3,F4):
    pass


print(F5.__mro__)

