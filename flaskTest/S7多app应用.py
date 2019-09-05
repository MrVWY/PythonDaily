#from werkzeug.wsgi import DispatcherMiddleware
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
from  flask import Flask

app1 = Flask('app01')
app2 = Flask('app02')

@app1.route('/index1')
def index1():
    return 'index1'


@app2.route('/index2')
def  index2():
    return 'index2'

app = DispatcherMiddleware(app1,{
    '/sec':app2,
})

if __name__ == '__main__':
    run_simple('localhost',5000,app)