import functools

def a(func):
    @functools.wraps(func)  #帮助我们设置函数的元信息
    def inner(*args,**kwargs):
        return func(*args,**kwargs)
    return inner

@a
def f1():
    pass

print(f1.__name__)


def b(func):
    def inner(*args,**kwargs):
        return func(*args,**kwargs)
    return inner

@b
def f2():
    pass

print(f2.__name__)


class Foo(object):

    def __setattr__(self, key, value):
        print(key,value)

    def __getattr__(self, item):
        print(item)

obj = Foo()
obj.x = 123
obj.x


from functools import partial

class Foo(object):

    def __init__(self):
        self.request = "request"
        self.session = "session"

foo = Foo()

def func(args):
    return getattr(foo,args)

re_func = partial(func,'request')
se_func = partial(func,'session')

print(re_func(),se_func())