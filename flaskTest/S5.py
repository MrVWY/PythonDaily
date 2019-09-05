from flask import Flask,request,g,render_template
app = Flask(__name__)

@app.before_request
def process_request1(*args,**kwargs):
    g.xxxx= 123
    print('process_request 1 来了')
    return g

@app.route('/index',methods=['GET'])
def index():
    print(request)  #LocalProxy.__str__  --> str(LocalProxy._get_current_object)  -->  调用偏函数  ctx.request
    print(request.method)  #LocalProxy.__getattr__  -->  str(LocalProxy._get_current_object)  -->  调用偏函数  ctx.request
                                                        # getattr(self._get_current_object(),name)      -->ctx.request.method
    print('index函数',g.xxxx)
    #return 'Index'
    return  render_template()

if __name__ == '__main__':
    app.__call__
    app.run()

    foo = type('foo',(object,),{})