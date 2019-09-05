from flask import Flask,request
app = Flask(__name__)

@app.before_request
def process_request1(*args,**kwargs):
    print('process_request 1 来了')

@app.before_request
def process_request2(*args,**kwargs):
    print('process_request 2 来了')

@app.after_request
def process_response1(*args,**kwargs):
    print('process_response 1 来了')

@app.after_request
def process_response2(*args,**kwargs):
    print('process_response 2 来了')

@app.errorhandler(404)
def error_404(arg):
    return '404 error'

@app.route('/index',methods=['GET'])
def index():
    print('index函数')
    return 'Index'

if __name__ == '__main__':
    app.run()