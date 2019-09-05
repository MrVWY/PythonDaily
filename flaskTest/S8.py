
class foo(object):
    def open(self):
        pass

    def fetch(self,msg):
        pass

    def close(self):
        pass

    def __enter__(self):
        self.open()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
        return self

with  foo() as obj:   #自动调用类中的__enter__方法，obj就是__enter__返回值
    obj.fetch('ssssss')
    #当执行完毕后，自动调用类__exit__方法